import json
import math
import os
from bs4 import BeautifulSoup
import requests
import csv
import re

from utilities.dataviz import plot_ratings

def get_map_score(match, file, stage):
  requesturl = "https://bo3.gg"+match
  print(requesturl)
  r = requests.get(requesturl)
  data = r.text
  soup = BeautifulSoup(data, 'lxml')
  teams = soup.find_all('div', class_='name')
  team1 = teams[0].string.strip()
  team2 = teams[1].string.strip()
  team1_scores = []
  team2_scores = []
  scores = soup.find_all('div', class_='c-match-score-map score')
  for score in scores:
    team1_scores.append(score.find('span', class_='score-1'))
    team2_scores.append(score.find('span', class_='score-2'))

  #team1_scores.pop(0)
  #team2_scores.pop(0)

  with open(file, 'a', encoding='utf-8', newline='') as csvfile:
    fieldnames = ['loser', 'winner', 'margin', 'stage']
    matchwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    for t1rounds, t2rounds in zip(team1_scores, team2_scores):
      if int(t1rounds.string) > int(t2rounds.string):
        matchwriter.writerow({'loser': team2, 'winner': team1, 'margin': int(t1rounds.string) - int(t2rounds.string), 'stage': stage})
      else:
        matchwriter.writerow({'loser': team1, 'winner': team2, 'margin': int(t2rounds.string) - int(t1rounds.string), 'stage': stage})

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

  matches = soup2.find_all('a', class_='c-global-match-link table-cell')
  stages = soup2.find_all('p', class_='system')
  for match, stage in reversed(list(zip(matches, stages))):
    get_map_score(match.get('href'), 'data/matches-'+event+'.csv', stage.string.strip())

  matches = soup.find_all('a', class_='c-global-match-link table-cell')
  stages = soup.find_all('p', class_='system')
  for match, stage in reversed(list(zip(matches, stages))):
    get_map_score(match.get('href'), 'data/matches-'+event+'.csv', stage.string.strip())

def update_match_results(event, generate_gif):
  print('---Starting ' + event + ' ---')
  data_path = "data/" + event
  if not os.path.exists(data_path):
    os.makedirs(data_path)
  with open('data/teams.json', encoding='utf-8') as encoded_teams:
    teams = json.load(encoded_teams)
  filename = "data/matches-" + event + ".csv"
  with open(filename, encoding='utf-8', newline='') as csvfile:
    matchreader = csv.DictReader(csvfile)
    i = 0
    for row in matchreader:
      winner = row['winner']
      loser = row['loser']
      margin = row['margin']
      if winner == 'Giants Gaming':
        winner = 'GIANTX'
      if loser == 'Giants Gaming':
        loser = 'GIANTX'
      if winner == 'Titan Esports Club':
        winner = 'TEC Esports'
      if loser == 'Titan Esports Club':
        loser = 'TEC Esports'
      if winner in teams:
        winner_rating = teams[winner]['rating']
        loser_rating = teams[loser]['rating']

        R1 = winner_rating
        R2 = loser_rating
        Q1 = math.pow(10, (R1/400))
        Q2 = math.pow(10, (R2/400))
        E1 = Q1/(Q1+Q2)
        E2 = Q2/(Q1+Q2)

        if 'regular' in row['stage']:
          k = 32
        elif 'lockin' in event:
          k = 16
        else:
          k = 24
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
        if(generate_gif):
          plot_ratings(event, str(i), teams)
        i += 1
        print(winner + ' ('+str(winner_rating)+' -> '+str(teams[winner]['rating'])+')' + ' vs. ' + loser + ' ('+str(loser_rating)+' -> '+str(teams[loser]['rating'])+') by ' + margin + ' rounds')
      else:
        print("Skipping show match: " + winner + " vs. " + loser)

  
  plot_ratings(event, "end", teams)
  with open('data/teams.json', 'w') as outfile:
    json.dump(teams, outfile, indent=2)

  print('---Ending ' + event + ' ---')