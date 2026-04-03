import json
import math
import os
from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

from utilities.dataviz import plot_ratings

def get_map_score(match, file):
  requesturl = "https://www.vlr.gg"+match
  print(requesturl)
  r = requests.get(requesturl)
  data = r.text
  soup = BeautifulSoup(data, 'lxml')
  teams = soup.find_all('div', class_='wf-title-med')
  team1 = teams[0].text.strip()
  team2 = teams[1].text.strip()
  team1_scores = []
  team1_attacks = []
  team1_defenses = []
  team1_kills = []
  team1_deaths = []
  team1_assists = []
  team1_mps = []
  team2_scores = []
  team2_attacks = []
  team2_defenses = []
  team2_kills = []
  team2_deaths = []
  team2_assists = []
  team2_mps = []
  scores = soup.find_all('div', class_='score')
  attacks = soup.find_all(lambda tag: tag.name == 'span' and tag.get('class') == ['mod-t'])
  defenses = soup.find_all(lambda tag: tag.name == 'span' and tag.get('class') == ['mod-ct'])
  maps = soup.find_all('div', class_='vm-stats-game')
  maps.pop(1)
  if len(maps) > 1:
    i = 1
    for map in maps:
      kills = map.find_all('td', class_='mod-vlr-kills')
      deaths = map.find_all('td', class_='mod-vlr-deaths')
      assists = map.find_all('td', class_='mod-vlr-assists')
      rounds = map.find_all('div', class_='vlr-rounds-row-col')
      map_points = []
      map_point = False
      for round in rounds:
        round_score = str(round.get('title'))
        if "12" in round_score:
          map_point = True
        if map_point:
          if '-' in round_score:
            round_score_split = round_score.split('-')
            if round_score_split[0] != round_score_split[1]:
              map_points.append(round_score)
      map_points.pop()
      team1kills = 0
      team1deaths = 0
      team1assists = 0
      team1mps = 0
      team2kills = 0
      team2deaths = 0
      team2assists = 0
      team2mps = 0
      index = 0
      for mp in map_points:
        split = mp.split('-')
        if int(split[0]) > int(split[1]):
          team1mps += 1
        else:
          team2mps += 1
      for kill, death, assist in zip(kills, deaths, assists):
        if index < 5:
          team1kills += int(kill.find('span', class_='mod-both').string)
          team1deaths += int(death.find('span', class_='mod-both').string)
          team1assists += int(assist.find('span', class_='mod-both').string)
        else:
          team2kills += int(kill.find('span', class_='mod-both').string)
          team2deaths += int(death.find('span', class_='mod-both').string)
          team2assists += int(assist.find('span', class_='mod-both').string)
        index+=1
      team1_kills.append(team1kills)
      team1_deaths.append(team1deaths)
      team1_assists.append(team1assists)
      team1_mps.append(team1mps)
      team2_kills.append(team2kills)
      team2_deaths.append(team2deaths)
      team2_assists.append(team2assists)
      team2_mps.append(team2mps)
      i+=1

    index = 0
    for score, attack, defense in zip(scores, attacks, defenses):
      if index%2==0:
        team1_scores.append(score)
        team1_attacks.append(attack)
        team1_defenses.append(defense)
      else:
        team2_scores.append(score)
        team2_attacks.append(attack)
        team2_defenses.append(defense)
      index+=1

  #team1_scores.pop(0)
  #team2_scores.pop(0)

  with open(file, 'a', encoding='utf-8', newline='') as csvfile:
    fieldnames = ['loser', 'winner', 'margin', 
                  'loser rounds', 'loser attack rounds', 'loser attack rounds won', 
                  'loser defense rounds', 'loser defense rounds won', 'loser overtime rounds won', 
                  'loser kills', 'loser deaths', 'loser assists', 'loser map points',
                  'winner rounds', 'winner attack rounds', 'winner attack rounds won', 
                  'winner defense rounds', 'winner defense rounds won', 'winner overtime rounds won', 
                  'winner kills', 'winner deaths', 'winner assists', 'winner map points',
                  'total rounds', 'overtime rounds']
    matchwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    for t1rounds, t2rounds, t1attacks, t2attacks, t1defenses, t2defenses, t1kills, t2kills, t1deaths, t2deaths, t1assists, t2assists, t1mps, t2mps in zip(team1_scores, team2_scores, team1_attacks, team2_attacks, team1_defenses, team2_defenses, team1_kills, team2_kills, team1_deaths, team2_deaths, team1_assists, team2_assists, team1_mps, team2_mps):
      if int(t1rounds.string) > int(t2rounds.string):
        matchwriter.writerow({'loser': team2, 'winner': team1, 'margin': int(t1rounds.string) - int(t2rounds.string), 
                              'loser rounds': int(t2rounds.string), 'loser attack rounds': int(t2attacks.string)+int(t1defenses.string), 'loser attack rounds won': int(t2attacks.string), 'loser defense rounds': int(t2defenses.string)+int(t1attacks.string), 
                              'loser defense rounds won': int(t2defenses.string), 'loser overtime rounds won': 0 if (int(t2rounds.string) < 12) else int(t2rounds.string)-12, 'loser kills': t2kills, 'loser deaths': t2deaths, 'loser assists': t2assists, 'loser map points': t2mps,
                              'winner rounds': int(t1rounds.string), 'winner attack rounds': int(t1attacks.string)+int(t2defenses.string), 'winner attack rounds won': int(t1attacks.string), 'winner defense rounds': int(t1defenses.string)+int(t2attacks.string), 
                              'winner defense rounds won': int(t1defenses.string), 'winner overtime rounds won': 0 if int(t1rounds.string) == 13 else int(t1rounds.string)-12, 'winner kills': t1kills, 'winner deaths': t1deaths, 'winner assists': t1assists, 'winner map points': t1mps,
                              'total rounds': int(t1rounds.string) + int(t2rounds.string), 'overtime rounds': 0 if int(t1rounds.string) == 13 else (int(t1rounds.string)-12)+(int(t2rounds.string)-12)})
      else:
        matchwriter.writerow({'loser': team1, 'winner': team2, 'margin': int(t2rounds.string) - int(t1rounds.string), 
                              'loser rounds': int(t1rounds.string), 'loser attack rounds': int(t1attacks.string)+int(t2defenses.string), 'loser attack rounds won': int(t1attacks.string), 'loser defense rounds': int(t1defenses.string)+int(t2attacks.string), 
                              'loser defense rounds won': int(t1defenses.string), 'loser overtime rounds won': 0 if (int(t1rounds.string) < 12) else int(t1rounds.string)-12, 'loser kills': t1kills, 'loser deaths': t1deaths, 'loser assists': t1assists, 'loser map points': t1mps,
                              'winner rounds': int(t2rounds.string), 'winner attack rounds': int(t2attacks.string)+int(t1defenses.string), 'winner attack rounds won': int(t2attacks.string), 'winner defense rounds': int(t2defenses.string)+int(t1attacks.string), 
                              'winner defense rounds won': int(t2defenses.string), 'winner overtime rounds won': 0 if int(t2rounds.string) == 13 else int(t2rounds.string)-12, 'winner kills': t2kills,  'winner deaths': t2deaths, 'winner assists': t2assists, 'winner map points': t2mps,
                              'total rounds': int(t2rounds.string) + int(t1rounds.string), 'overtime rounds': 0 if int(t2rounds.string) == 13 else (int(t2rounds.string)-12)+(int(t1rounds.string)-12)})

def create_matches_file(event):
  requesturl = "https://www.vlr.gg/event/matches/"+event+"/?series_id=all"
  r = requests.get(requesturl)
  data = r.text
  soup = BeautifulSoup(data, 'lxml')

  with open('data/matches-'+event.replace('/', '-')+'.csv', 'w', encoding='utf-8', newline='') as csvfile:
    fieldnames = ['loser', 'winner', 'margin', 
                  'loser rounds', 'loser attack rounds', 'loser attack rounds won', 
                  'loser defense rounds', 'loser defense rounds won', 'loser overtime rounds won', 
                  'loser kills', 'loser deaths', 'loser assists', 'loser map points',
                  'winner rounds', 'winner attack rounds', 'winner attack rounds won', 
                  'winner defense rounds', 'winner defense rounds won', 'winner overtime rounds won', 
                  'winner kills', 'winner deaths', 'winner assists', 'winner map points',
                  'total rounds', 'overtime rounds']
    matchwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    matchwriter.writeheader()

  matches = soup.find_all('a', class_='match-item')
  for match in matches:
    try:
      get_map_score(match.get('href'), 'data/matches-'+event.replace('/', '-')+'.csv')
    except:
      print("Failed to get map score for " + match.get('href'))

def create_table(year):
  print('---Creating Table---')
  with open('data/teams.json', encoding='utf-8') as encoded_teams:
    eteams = json.load(encoded_teams)

  teams = []
  regions = []
  maps = []
  winlosspcts = []
  rpgs = []
  opprpgs = []
  movs = []
  sos = []
  atkwinpcts = []
  defwinpcts = []
  kprs = []
  dprs = []
  aprs = []
  mps = []
  mppcts = []
  for team in eteams:
    #if eteams[team]['maps'] > 15:
      rpg = eteams[team]['rounds won']/eteams[team]['maps']
      opprpg = (eteams[team]['total rounds']-eteams[team]['rounds won'])/eteams[team]['maps']
      mov = rpg - opprpg
      atkwinpct = eteams[team]['attack rounds won']/eteams[team]['attack rounds']
      defwinpct = eteams[team]['defense rounds won']/eteams[team]['defense rounds']
      kpr = eteams[team]['kills']/eteams[team]['total rounds']
      dpr = eteams[team]['deaths']/eteams[team]['total rounds']
      apr = eteams[team]['assists']/eteams[team]['total rounds']
      mp = eteams[team]['map points']
      mppct = eteams[team]['wins']/eteams[team]['map points']
      teams.append(team)
      regions.append(eteams[team]['league'])
      maps.append(eteams[team]['maps'])
      winlosspcts.append(eteams[team]['wins']/eteams[team]['maps'])
      rpgs.append(rpg)
      opprpgs.append(opprpg)
      movs.append(mov)
      sos.append(eteams[team]['strength of schedule'])
      atkwinpcts.append(atkwinpct)
      defwinpcts.append(defwinpct)
      kprs.append(kpr)
      dprs.append(dpr)
      aprs.append(apr)
      mps.append(mp)
      mppcts.append(mppct)

  df = pd.DataFrame(
    {
      "Team": teams,
      "Region": regions,
      "Maps": maps,
      "W-L %": winlosspcts,
      "Rounds/Game": rpgs,
      "Opp. Rounds/Game": opprpgs,
      "Atk. Win %": atkwinpcts,
      "Def. Win %": defwinpcts,
      "MoV": movs,
      "SoS": sos,
      "Kills/Round": kprs,
      "Deaths/Round": dprs,
      "Assists/Round": aprs,
      "Map Points": mps,
      "MP Win %": mppcts
    }
  )
  df.to_excel('data/Valorant Ratings.xlsx', sheet_name=year, index=False)
  
  print('---Table Created---')

def calculate_sos():
  print('---Starting Strength of Schedule Calculation---')
  with open('data/teams.json', encoding='utf-8') as encoded_teams:
    teams = json.load(encoded_teams)

  for team in teams:
    oppmov = 0
    for opponent in teams[team]["opponents"]:
      oppmov += teams[opponent]["rounds won"]/teams[opponent]["maps"] - (teams[opponent]["total rounds"] - teams[opponent]["rounds won"])/teams[opponent]["maps"]
    sos = oppmov/teams[team]["maps"]
    teams[team]['strength of schedule'] = sos

  with open('data/teams.json', 'w') as outfile:
    json.dump(teams, outfile, indent=2)
  print('---Ending Strength of Schedule Calculation---')

def update_match_results(event, generate_gif):
  print('---Starting ' + event + ' ---')
  # data_path = "data/" + event.replace('/', '-')
  # if not os.path.exists(data_path):
  #   os.makedirs(data_path)
  with open('data/teams.json', encoding='utf-8') as encoded_teams:
    teams = json.load(encoded_teams)
  # plot_ratings(event.replace('/', '-'), "start", teams)
  filename = "data/matches-" + event.replace('/', '-') + ".csv"
  with open(filename, encoding='utf-8', newline='') as csvfile:
    matchreader = csv.DictReader(csvfile)
    i = 0
    for row in matchreader:
      winner = row['winner'].strip("'")
      loser = row['loser'].strip("'")
      margin = row['margin']
      loserrounds = row['loser rounds']
      loserattackrounds = row['loser attack rounds']
      loserattackroundswon = row['loser attack rounds won']
      loserdefenserounds = row['loser defense rounds']
      loserdefenseroundswon = row['loser defense rounds won']
      loserovertimeroundswon = row['loser overtime rounds won']
      winnerrounds = row['winner rounds']
      winnerattackrounds = row['winner attack rounds']
      winnerattackroundswon = row['winner attack rounds won']
      winnerdefenserounds = row['winner defense rounds']
      winnerdefenseroundswon = row['winner defense rounds won']
      winnerovertimeroundswon = row['winner overtime rounds won']
      winnerkills = row['winner kills']
      winnerdeaths = row['winner deaths']
      winnerassists = row['winner assists']
      winnermappoints = row['winner map points']
      loserkills = row['loser kills']
      loserdeaths = row['loser deaths']
      loserassists = row['loser assists']
      losermappoints = row['loser map points']
      totalrounds = row['total rounds']
      overtimerounds = row['overtime rounds']
      if winner not in teams:
        team = {
          "assists": 0,
          "attack rounds": 0,
          "attack rounds won": 0,
          "deaths": 0,
          "defense rounds": 0,
          "defense rounds won": 0,
          "kills": 0,
          "league": "Unspecified",
          "losses": 0,
          "map points": 0,
          "maps": 0,
          "opponents": [],
          "overtime rounds": 0,
          "overtime rounds won": 0,
          "rating": 1000,
          "rounds won": 0,
          "strength of schedule": 0,
          "total rounds": 0,
          "wins": 0
        }
        teams[winner] = team
        if any(q in event for q in ['korea', 'japan', 'sea', 'asia-pacific', 'east-asia', 'pacific']):
          teams[winner]['league'] = 'Pacific'
        elif any(q in event for q in ['turkey', 'europe', 'emea']):
          teams[winner]['league'] = 'EMEA'
        elif any(q in event for q in ['north-america', 'latam', 'brazil', 'latin-america']):
          teams[winner]['league'] = 'Americas'
        elif any(q in event for q in ['china']):
          teams[winner]['league'] = 'China'

      if loser not in teams:
        team = {
          "assists": 0,
          "attack rounds": 0,
          "attack rounds won": 0,
          "deaths": 0,
          "defense rounds": 0,
          "defense rounds won": 0,
          "kills": 0,
          "league": "Unspecified",
          "losses": 0,
          "map points": 0,
          "maps": 0,
          "opponents": [],
          "overtime rounds": 0,
          "overtime rounds won": 0,
          "rating": 1000,
          "rounds won": 0,
          "strength of schedule": 0,
          "total rounds": 0,
          "wins": 0
        }
        teams[loser] = team
        if any(q in event for q in ['korea', 'japan', 'sea', 'asia-pacific', 'east-asia', 'pacific']):
          teams[loser]['league'] = 'Pacific'
        elif any(q in event for q in ['turkey', 'europe', 'emea']):
          teams[loser]['league'] = 'EMEA'
        elif any(q in event for q in ['north-america', 'latam', 'brazil', 'latin-america']):
          teams[loser]['league'] = 'Americas'
        elif any(q in event for q in ['china']):
          teams[loser]['league'] = 'China'


      winner_rating = teams[winner]['rating']
      loser_rating = teams[loser]['rating']

      R1 = winner_rating
      R2 = loser_rating
      Q1 = math.pow(10, (R1/400))
      Q2 = math.pow(10, (R2/400))
      E1 = Q1/(Q1+Q2)
      E2 = Q2/(Q1+Q2)

      if 'evolution' in event:
        k = 16
      else:
        k = 32
      if int(margin) == 2:
        k *= 0.25
      elif int(margin) > 2 and int(margin) <= 5:
        k *= 0.5
      elif int(margin) > 5 and int(margin) <= 9:
        k *= 1
      else:
        k *= 2

      R1 = R1 + k*(1-E1)
      R2 = R2 + k*(0-E2)
      teams[winner]['rating'] = int(R1)
      teams[loser]['rating'] = int(R2)
      teams[winner]['wins'] += 1
      teams[loser]['losses'] += 1
      teams[winner]['maps'] += 1
      teams[loser]['maps'] += 1
      teams[winner]['kills'] += int(winnerkills)
      teams[winner]['deaths'] += int(winnerdeaths)
      teams[winner]['assists'] += int(winnerassists)
      teams[winner]['map points'] += int(winnermappoints)
      teams[loser]['kills'] += int(loserkills)
      teams[loser]['deaths'] += int(loserdeaths)
      teams[loser]['assists'] += int(loserassists)
      teams[loser]['map points'] += int(losermappoints)
      teams[winner]['rounds won'] += int(winnerrounds)
      teams[loser]['rounds won'] += int(loserrounds)
      teams[winner]['attack rounds'] += int(winnerattackrounds)
      teams[loser]['attack rounds'] += int(loserattackrounds)
      teams[winner]['defense rounds'] += int(winnerdefenserounds)
      teams[loser]['defense rounds'] += int(loserdefenserounds)
      teams[winner]['attack rounds won'] += int(winnerattackroundswon)
      teams[loser]['attack rounds won'] += int(loserattackroundswon)
      teams[winner]['defense rounds won'] += int(winnerdefenseroundswon)
      teams[loser]['defense rounds won'] += int(loserdefenseroundswon)
      teams[winner]['overtime rounds won'] += int(winnerovertimeroundswon)
      teams[loser]['overtime rounds won'] += int(loserovertimeroundswon)
      teams[winner]['overtime rounds'] += int(overtimerounds)
      teams[loser]['overtime rounds'] += int(overtimerounds)
      teams[winner]['total rounds'] += int(totalrounds)
      teams[loser]['total rounds'] += int(totalrounds)
      teams[winner]['opponents'].append(loser)
      teams[loser]['opponents'].append(winner)
      if(generate_gif):
        plot_ratings(event, str(i), teams)
      i += 1
      print(winner + ' ('+str(winner_rating)+' -> '+str(teams[winner]['rating'])+')' + ' vs. ' + loser + ' ('+str(loser_rating)+' -> '+str(teams[loser]['rating'])+') by ' + margin + ' rounds')

  
  # plot_ratings(event.replace('/', '-'), "end", teams)
  with open('data/teams.json', 'w') as outfile:
    json.dump(teams, outfile, indent=2)

  print('---Ending ' + event.replace('/', '-') + ' ---')