import json
import math
import os
from bs4 import BeautifulSoup
import requests
import csv
import re

from utilities.dataviz import plot_ratings

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
    fieldnames = ['loser', 'winner', 'margin', 'stage']
    matchwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    matchwriter.writeheader()

    regex = re.compile('score-[1-2]')
    losers = soup2.find_all(lambda tag: tag.name == 'div' and tag.get('class') == ['c-match__team'])
    winners = soup2.find_all('div', class_='c-match__team winner')
    winner_maps = soup2.find_all('span', class_='winner')
    loser_maps = soup2.find_all('span', class_=regex)
    loser_maps[:] = [x for x in loser_maps if ("winner" not in x)]
    stages = soup2.find_all('p', class_='system')
    for loser, winner, wmaps, lmaps, stage in reversed(list(zip(losers, winners, winner_maps, loser_maps, stages))):
      matchwriter.writerow({'loser': loser.div.string.strip(), 'winner': winner.div.string.strip(), 'margin': int(wmaps.string) - int(lmaps.string), 'stage': stage.string.strip()})

    losers = soup.find_all(lambda tag: tag.name == 'div' and tag.get('class') == ['c-match__team'])
    winners = soup.find_all('div', class_='c-match__team winner')
    winner_maps = soup.find_all('span', class_='winner')
    loser_maps = soup.find_all('span', class_=regex)
    loser_maps[:] = [x for x in loser_maps if "winner" not in str(x)]
    stages = soup.find_all('p', class_='system')
    for loser, winner, wmaps, lmaps, stage in reversed(list(zip(losers, winners, winner_maps, loser_maps, stages))):
      matchwriter.writerow({'loser': loser.div.string.strip(), 'winner': winner.div.string.strip(), 'margin': int(wmaps.string) - int(lmaps.string), 'stage': stage.string.strip()})

def update_match_results(event, generate_gif):
  print('---Starting ' + event + ' ---')
  data_path = "data/" + event
  if not os.path.exists(data_path):
    os.makedirs(data_path)
  with open('data/teams.json', encoding='utf-8') as encoded_teams:
    teams = json.load(encoded_teams)
  with open('data/accuracy.json', encoding='utf-8') as accuracy:
    acc = json.load(accuracy)
  filename = "data/matches-" + event + ".csv"
  with open(filename, encoding='utf-8', newline='') as csvfile:
    matchreader = csv.DictReader(csvfile)
    i = 0
    for row in matchreader:
      winner = row['winner']
      loser = row['loser']
      margin = row['margin']
      if winner in teams:
        winner_rating = teams[winner]['rating']
        loser_rating = teams[loser]['rating']

        if winner_rating > loser_rating:
          acc[event]['correct'] += 1
          print("CORRECT: " + winner + ' ('+str(winner_rating)+')' + ' vs. ' + loser + ' ('+str(loser_rating)+')')
        elif winner_rating == loser_rating:
          print("PUSH: " + winner + ' ('+str(winner_rating)+')' + ' vs. ' + loser + ' ('+str(loser_rating)+')')
        else:
          print("INCORRECT: " + winner + ' ('+str(winner_rating)+')' + ' vs. ' + loser + ' ('+str(loser_rating)+')')
        acc[event]['total'] += 1

        R1 = winner_rating
        R2 = loser_rating
        Q1 = math.pow(10, (R1/400))
        Q2 = math.pow(10, (R2/400))
        E1 = Q1/(Q1+Q2)
        E2 = Q2/(Q1+Q2)

        if 'china' in event:
          k = 8
        elif 'regular' in row['stage']:
          k = 16
        elif 'lockin' in event:
          k = 8
        else:
          k = 12
        if int(margin) >= 2:
          k += 12
        R1 = R1 + k*(1-E1)
        R2 = R2 + k*(0-E2)
        teams[winner]['rating'] = int(R1)
        teams[loser]['rating'] = int(R2)
        teams[winner]['wins'] += 1
        teams[loser]['losses'] += 1
        if(generate_gif):
          plot_ratings(event, str(i), teams)
        i += 1
      else:
        print("Skipping show match: " + winner + " vs. " + loser)

  with open('data/teams.json', 'w') as outfile:
    json.dump(teams, outfile, indent=2)

  if acc[event]['total'] != 0:
    acc[event]['percentage'] = (acc[event]['correct']/acc[event]['total']) * 100
  with open('data/accuracy.json', 'w') as outfile:
    json.dump(acc, outfile, indent=2)

  print('---Ending ' + event + ' ---')