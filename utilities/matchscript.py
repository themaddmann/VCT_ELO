import json
import math
from bs4 import BeautifulSoup
import requests
import csv

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
    fieldnames = ['loser', 'winner']
    matchwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    matchwriter.writeheader()

    losers = soup2.find_all(lambda tag: tag.name == 'div' and tag.get('class') == ['c-match__team'])
    winners = soup2.find_all('div', class_='c-match__team winner')
    for loser, winner in reversed(list(zip(losers, winners))):
      matchwriter.writerow({'loser': loser.div.string, 'winner': winner.div.string})

    losers = soup.find_all(lambda tag: tag.name == 'div' and tag.get('class') == ['c-match__team'])
    winners = soup.find_all('div', class_='c-match__team winner')
    for loser, winner in reversed(list(zip(losers, winners))):
      matchwriter.writerow({'loser': loser.div.string, 'winner': winner.div.string})

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
      if winner in teams:
        winner_rating = teams[winner]['rating']
        loser_rating = teams[loser]['rating']

        if winner_rating > loser_rating:
          acc['correct'] += 1
          print("CORRECT: " + winner + ' ('+str(winner_rating)+')' + ' vs. ' + loser + ' ('+str(loser_rating)+')')
        elif winner_rating == loser_rating:
          acc['correct'] += 0.5
          print("PUSH: " + winner + ' ('+str(winner_rating)+')' + ' vs. ' + loser + ' ('+str(loser_rating)+')')
        else:
          print("INCORRECT: " + winner + ' ('+str(winner_rating)+')' + ' vs. ' + loser + ' ('+str(loser_rating)+')')
        acc['total'] += 1

        R1 = winner_rating
        R2 = loser_rating
        Q1 = math.pow(10, (R1/400))
        Q2 = math.pow(10, (R2/400))
        E1 = Q1/(Q1+Q2)
        E2 = Q2/(Q1+Q2)

        if ('league') in event:
          k = 20
        elif ('last') in event:
          k = 30
        else:
          k = 40
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

  acc['percentage'] = (acc['correct']/acc['total']) * 100
  with open('data/accuracy.json', 'w') as outfile:
    json.dump(acc, outfile, indent=2)

  print('---Ending ' + event + ' ---')