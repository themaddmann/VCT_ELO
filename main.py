from utilities.dataviz import plot_ratings
from utilities.matchscript import create_matches_file, update_match_results

if __name__ == '__main__':

  #create_matches_file("vct-lockin-sao-paulo-2023")
  update_match_results("vct-lockin-sao-paulo-2023")
  plot_ratings("Lock In")
  
  #create_matches_file("vct-americas-league-2023")
  update_match_results("vct-americas-league-2023")
  #create_matches_file("vct-emea-league-2023")
  update_match_results("vct-emea-league-2023")
  #create_matches_file("vct-pacific-league-2023")
  update_match_results("vct-pacific-league-2023")
  plot_ratings("Regular Season")
  
  #create_matches_file("vct-masters-tokyo-2023")
  update_match_results("vct-masters-tokyo-2023")
  plot_ratings("Masters Tokyo")
  
  #create_matches_file("vct-americas-last-chance-qualifier-2023")
  update_match_results("vct-americas-last-chance-qualifier-2023")
  #create_matches_file("vct-emea-last-chance-qualifier-2023")
  update_match_results("vct-emea-last-chance-qualifier-2023")
  #create_matches_file("vct-pacific-last-chance-qualifier-2023")
  update_match_results("vct-pacific-last-chance-qualifier-2023")
  #create_matches_file("vct-china-qualifier-2023")
  update_match_results("vct-china-qualifier-2023")
  plot_ratings("LCQ")
  
  #create_matches_file("valorant-champions-2023")
  update_match_results("valorant-champions-2023")
  plot_ratings("Champions")