import json
import matplotlib.pyplot as plt
from adjustText import adjust_text

def plot_ratings(event):
  with open('data/teams.json', encoding='utf-8') as file:
    teams = json.load(file)

  names = []
  ratings = []
  leagues = []
  color = ''
  plt.figure(figsize=(20,10))
  for team in teams:
    if teams[team]['league'] == "skip":
      continue
    if int(teams[team]["wins"]) + int(teams[team]["losses"]) == 0:
      continue
    else:
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
  plt.title('Post ' + event + ' Ratings')
  plt.xlabel('League')
  plt.ylabel('Rating')
  adjust_text(texts, arrowprops=dict(arrowstyle='-', color='k', lw=0.5), min_arrow_len=25)
  plt.savefig("data/post-"+event+"-ratings.pdf", format="pdf", bbox_inches="tight")