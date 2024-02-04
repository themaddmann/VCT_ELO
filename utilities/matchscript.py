import json
import math
from bs4 import BeautifulSoup
import requests
import csv
import re

def create_matches_file(event):
  requesturl = "https://bo3.gg/valorant/tournaments/"+event+"/results"
  r = requests.get(requesturl)
  data = r.text
  soup = BeautifulSoup(data, 'lxml')


  requesturl = "https://bo3.gg/valorant/tournaments/"+event+"/results?page=2"
  r = requests.get(requesturl)
  data = r.text
  soup2 = BeautifulSoup(data, 'lxml')

  with open('data/matches-'+event+'.csv', 'w', encoding='utf-8', newline='') as csvfile:
    fieldnames = ['loser', 'winner', 'margin']
    matchwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    matchwriter.writeheader()

    regex = re.compile('score-[1-2]')
    losers = soup2.find_all(lambda tag: tag.name == 'div' and tag.get('class') == ['c-match__team'])
    winners = soup2.find_all('div', class_='c-match__team winner')
    winner_maps = soup2.find_all('span', class_='winner')
    loser_maps = soup2.find_all('span', class_=regex)
    loser_maps[:] = [x for x in loser_maps if ("winner" not in x)]
    for loser, winner, wmaps, lmaps in reversed(list(zip(losers, winners, winner_maps, loser_maps))):
      matchwriter.writerow({'loser': loser.div.string.strip(), 'winner': winner.div.string.strip(), 'margin': int(wmaps.string) - int(lmaps.string)})

    losers = soup.find_all(lambda tag: tag.name == 'div' and tag.get('class') == ['c-match__team'])
    winners = soup.find_all('div', class_='c-match__team winner')
    winner_maps = soup.find_all('span', class_='winner')
    loser_maps = soup.find_all('span', class_=regex)
    loser_maps[:] = [x for x in loser_maps if "winner" not in str(x)]
    for loser, winner, wmaps, lmaps in reversed(list(zip(losers, winners, winner_maps, loser_maps))):
      matchwriter.writerow({'loser': loser.div.string.strip(), 'winner': winner.div.string.strip(), 'margin': int(wmaps.string) - int(lmaps.string)})

def update_match_results(event):
  print('---Starting ' + event + ' ---')
  with open('data/teams.json', encoding='utf-8') as encoded_teams:
    teams = json.load(encoded_teams)
  with open('data/accuracy.json', encoding='utf-8') as accuracy:
    acc = json.load(accuracy)
  filename = "data/matches-" + event + ".csv"
  with open(filename, encoding='utf-8', newline='') as csvfile:
    matchreader = csv.DictReader(csvfile)
    for row in matchreader:
      winner = row['winner']
      loser = row['loser']
      margin = row['margin']
      if winner in teams:
        winner_rating = teams[winner]['rating']
        loser_rating = teams[loser]['rating']

        if winner_rating > loser_rating:
          if 'champions' in event or 'americas' in event or 'emea' in event or 'pacific' in event or 'masters' in event:
            acc['correct'] += 1
          print("CORRECT: " + winner + ' ('+str(winner_rating)+')' + ' vs. ' + loser + ' ('+str(loser_rating)+')')
        elif winner_rating == loser_rating:
          print("PUSH: " + winner + ' ('+str(winner_rating)+')' + ' vs. ' + loser + ' ('+str(loser_rating)+')')
        else:
          print("INCORRECT: " + winner + ' ('+str(winner_rating)+')' + ' vs. ' + loser + ' ('+str(loser_rating)+')')
          
        if 'champions' in event or 'americas' in event or 'emea' in event or 'pacific' in event or 'masters' in event:
          acc['total'] += 1

        R1 = winner_rating
        R2 = loser_rating
        Q1 = math.pow(10, (R1/400))
        Q2 = math.pow(10, (R2/400))
        E1 = Q1/(Q1+Q2)
        E2 = Q2/(Q1+Q2)

        if 'last' in event or 'china' in event or 'lockin' in event:
          k = 16
        else:
          k = 24
        if int(margin) == 2:
          k *= 2
        elif int(margin) == 3:
          k *= 3
        R1 = R1 + k*(1-E1)
        R2 = R2 + k*(0-E2)
        teams[winner]['rating'] = int(R1)
        teams[loser]['rating'] = int(R2)
        teams[winner]['wins'] += 1
        teams[loser]['losses'] += 1
      else:
        print("Skipping show match: " + winner + " vs. " + loser)

  with open('data/teams.json', 'w') as outfile:
    json.dump(teams, outfile, indent=2)

  if acc['total'] != 0:
    acc['percentage'] = (acc['correct']/acc['total']) * 100
  with open('data/accuracy.json', 'w') as outfile:
    json.dump(acc, outfile, indent=2)

  print('---Ending ' + event + ' ---')