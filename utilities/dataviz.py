import json
import matplotlib.pyplot as plt
from adjustText import adjust_text

def plot_ratings_vs_wins(event):
  with open('data/teams.json', encoding='utf-8') as file:
    teams = json.load(file)

  names = []
  ratings = []
  games = []
  color = ''
  plt.figure(figsize=(20,10))
  for team in teams:
    names.append(team)
    ratings.append(teams[team]['rating'])
    games.append(teams[team]["wins"]+teams[team]["losses"])
    if teams[team]['league'] == 'Americas':
      color = 'tab:orange'
    elif teams[team]['league'] == 'EMEA':
      color = 'tab:olive'
    elif teams[team]['league'] == 'Pacific':
      color = 'tab:cyan'
    elif teams[team]['league'] == 'China':
      color = 'tab:red'
    plt.scatter((teams[team]["wins"]+teams[team]["losses"]), teams[team]['rating'], color=color)
  
  plt.legend(names, ncol=4)
  texts = [plt.text(games[i], ratings[i], names[i] + ' ('+str(ratings[i])+')', ha='center', va='center') for i in range(len(names))]
  plt.title('VCT Ratings')
  plt.xlabel('games played')
  plt.ylabel('rating')
  adjust_text(texts, arrowprops=dict(arrowstyle='-', color='k', lw=0.5), min_arrow_len=10)
  plt.savefig("data/post-"+event+"-ratings.pdf", format="pdf", bbox_inches="tight")