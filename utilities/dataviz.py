import json
import os
import matplotlib.pyplot as plt
import imageio
from adjustText import adjust_text
import numpy as np

def plot_preseason():
  event = "Pre-Kickoff 2024"
  game = "0"
  with open('data/teams.json', encoding='utf-8') as encoded_teams:
    teams = json.load(encoded_teams)
  plot_ratings(event, game, teams)

def plot_ratings(event, game, teams):
  names = []
  ratings = []
  leagues = []
  color = ''
  plt.figure(figsize=(20,10))
  for team in teams:
    if int(teams[team]["wins"]) + int(teams[team]["losses"]) > 0:
      names.append(team)
      ratings.append(teams[team]['rating'])
      leagues.append(teams[team]['league'])
      if teams[team]['league'] == 'Americas':
        color = 'tab:orange'
      elif teams[team]['league'] == 'EMEA':
        color = 'tab:olive'
      elif teams[team]['league'] == 'Pacific':
        color = 'tab:cyan'
      elif teams[team]['league'] == 'China':
        color = 'tab:red'
      plt.scatter(teams[team]["league"], teams[team]['rating'], color=color)
  
  texts = [plt.text(leagues[i], ratings[i], names[i] + ' ('+str(ratings[i])+')', size=7, ha='left', va='center') for i in range(len(names))]
  plt.title('VCT Ratings')
  plt.xlabel('League')
  plt.ylabel('Rating')
  adjust_text(texts, arrowprops=dict(arrowstyle='-', color='k', lw=0.5), min_arrow_len=25)
  data_path = "data/"+event
  if not os.path.exists(data_path):
    os.makedirs(data_path)
  plt.savefig(data_path+"/ratings-"+game+".png", format="png", bbox_inches="tight")
  plt.close()

def create_event_gif(event):
  folder = "data/"+event
  images = list()
  def get_sorted_files(item):
    item_path = os.path.join(folder, item)
    return os.path.getctime(item_path)
  for file in sorted(os.listdir(folder), key=get_sorted_files):
    file_path = os.path.join(folder, file)
    images.append(imageio.imread(file_path))

  for _ in range(10):
    images.append(imageio.imread(file_path))
  gif_path = "data/" + event + ".gif"
  imageio.mimsave(gif_path, images, fps=2, loop=0)
