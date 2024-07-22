from utilities.dataviz import create_event_gif, plot_preseason, plot_ratings
from utilities.matchscript import create_matches_file, get_map_score, update_match_results

if __name__ == '__main__':

  generate_gif = False
  #create_matches_file("valorant-champions-tour-2024-emea-stage-2")
  #update_match_results("vct-lockin-sao-paulo-2023", generate_gif)
  #update_match_results("vct-americas-league-2023", generate_gif)
  #update_match_results("vct-emea-league-2023", generate_gif)
  #update_match_results("vct-pacific-league-2023", generate_gif)
  #update_match_results("vct-masters-tokyo-2023", generate_gif)
  #update_match_results("vct-americas-last-chance-qualifier-2023", generate_gif)
  #update_match_results("vct-emea-last-chance-qualifier-2023", generate_gif)
  #update_match_results("vct-pacific-last-chance-qualifier-2023", generate_gif)
  #update_match_results("valorant-champions-2023", generate_gif)
  #update_match_results("valorant-champions-tour-2024-americas-kickoff", generate_gif)
  #update_match_results("valorant-champions-tour-2024-emea-kickoff", generate_gif)
  #update_match_results("valorant-champions-tour-2024-pacific-kickoff", generate_gif)
  #update_match_results("valorant-champions-tour-2024-china-kickoff", generate_gif)
  #update_match_results("valorant-champions-tour-2024-masters-madrid", generate_gif)
  #update_match_results("valorant-champions-tour-2024-americas-league-stage-1", generate_gif)
  #update_match_results("valorant-champions-tour-2024-emea-stage-1", generate_gif)
  #update_match_results("valorant-champions-tour-2024-pacific-stage-1", generate_gif)
  #update_match_results("valorant-champions-tour-2024-china-stage-1", generate_gif)
  #update_match_results("valorant-champions-tour-2024-masters-shanghai", generate_gif)
  update_match_results("valorant-champions-tour-2024-americas-league-stage-2", generate_gif)
  update_match_results("valorant-champions-tour-2024-emea-stage-2", generate_gif)
  update_match_results("valorant-champions-tour-2024-pacific-stage-2", generate_gif)
  update_match_results("valorant-champions-tour-2024-china-stage-2", generate_gif)
  #create_event_gif("valorant-champions-tour-2024-masters-madrid")

  #plot_preseason()