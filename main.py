from utilities.dataviz import create_event_gif, plot_preseason, plot_ratings
from utilities.matchscript import create_matches_file, get_map_score, create_matches_file, update_match_results, calculate_sos, create_table

if __name__ == '__main__':

  generate_gif = False

#   # 2021
  # create_matches_file('351/champions-tour-korea-stage-1-masters')
  # create_matches_file('342/champions-tour-turkey-stage-1-masters')
  # create_matches_file('334/champions-tour-europe-stage-1-masters')
  # create_matches_file('333/champions-tour-north-america-stage-1-masters')
  # create_matches_file('340/champions-tour-latam-stage-1-masters')
  # create_matches_file('352/champions-tour-japan-stage-1-masters')
  # create_matches_file('347/champions-tour-sea-stage-1-masters')
  # create_matches_file('338/champions-tour-brazil-stage-1-masters')

  # create_matches_file('441/champions-tour-japan-stage-2-challengers-finals')
  # create_matches_file('429/champions-tour-sea-stage-2-challengers-finals')
  # create_matches_file('426/champions-tour-korea-stage-2-challengers')
  # create_matches_file('376/champions-tour-stage-2-emea-challengers-playoffs')
  # create_matches_file('372/champions-tour-north-america-stage-2-challengers-finals')
  # create_matches_file('366/champions-tour-brazil-stage-2-challengers-finals')
  # create_matches_file('398/champions-tour-latam-stage-2-challengers-finals')
  # create_matches_file('353/valorant-champions-tour-stage-2-masters-reykjav-k')

  # create_matches_file('540/champions-tour-japan-stage-3-challengers-playoffs')
  # create_matches_file('595/champions-tour-korea-stage-3-challengers')
  # create_matches_file('578/champions-tour-north-america-stage-3-challengers-playoffs')
  # create_matches_file('621/champions-tour-latam-stage-3-challengers-playoffs')
  # create_matches_file('547/champions-tour-stage-3-emea-challengers-playoffs')
  # create_matches_file('536/champions-tour-brazil-stage-3-challengers-playoffs')
  # create_matches_file('570/champions-tour-sea-stage-3-challengers-playoffs')
  # create_matches_file('466/valorant-champions-tour-stage-3-masters-berlin')

  # create_matches_file('560/champions-tour-asia-pacific-last-chance-qualifier')
  # create_matches_file('559/champions-tour-emea-last-chance-qualifier')
  # create_matches_file('561/champions-tour-south-america-last-chance-qualifier')
  # create_matches_file('558/champions-tour-north-america-last-chance-qualifier')

  # create_matches_file('449/valorant-champions-2021')

#   # 2022
  # create_matches_file('884/champions-tour-asia-pacific-stage-1-challengers-playoffs')
  # create_matches_file('850/champions-tour-korea-stage-1-challengers')
  # create_matches_file('853/champions-tour-japan-stage-1-challengers-playoffs')
  # create_matches_file('854/champions-tour-stage-1-emea-challengers')
  # create_matches_file('799/champions-tour-north-america-stage-1-challengers')
  # create_matches_file('829/champions-tour-brazil-stage-1-challengers-1')
  # create_matches_file('925/champions-tour-latin-america-stage-1-playoffs')
  # create_matches_file('948/champions-tour-latam-br-stage-1-last-chance-qualifier')
  # create_matches_file('926/valorant-champions-tour-stage-1-masters-reykjav-k')
  
  # create_matches_file('1013/champions-tour-japan-stage-2-challengers-playoffs')
  # create_matches_file('998/champions-tour-korea-stage-2-challengers')
  # create_matches_file('1063/champions-tour-asia-pacific-stage-2-challengers-playoffs')
  # create_matches_file('984/champions-tour-emea-stage-2-challengers')
  # create_matches_file('911/champions-tour-brazil-stage-2-challengers')
  # create_matches_file('800/champions-tour-north-america-stage-2-challengers')
  # create_matches_file('1086/champions-tour-latin-america-stage-2-playoffs')
  # create_matches_file('1085/champions-tour-latam-br-stage-2-last-chance-qualifier')
  # create_matches_file('1014/valorant-champions-tour-stage-2-masters-copenhagen')
  
  # create_matches_file('1084/champions-tour-asia-pacific-last-chance-qualifier')
  # create_matches_file('1130/champions-tour-north-america-last-chance-qualifier')
  # create_matches_file('1083/champions-tour-east-asia-last-chance-qualifier')
  # create_matches_file('1117/champions-tour-emea-last-chance-qualifier')
  # create_matches_file('1111/champions-tour-south-america-last-chance-qualifier')
  # create_matches_file('1015/valorant-champions-2022')

# # 2023
  # create_matches_file('1188/champions-tour-2023-lock-in-s-o-paulo')

  # create_matches_file('1191/champions-tour-2023-pacific-league')
  # create_matches_file('1190/champions-tour-2023-emea-league')
  # create_matches_file('1189/champions-tour-2023-americas-league')
  # create_matches_file('1494/champions-tour-2023-masters-tokyo')

  # create_matches_file('1664/champions-tour-2023-champions-china-qualifier')
  # create_matches_file('1660/champions-tour-2023-pacific-last-chance-qualifier')
  # create_matches_file('1659/champions-tour-2023-emea-last-chance-qualifier')
  # create_matches_file('1658/champions-tour-2023-americas-last-chance-qualifier')
  # create_matches_file('1657/valorant-champions-2023')

#   # 2024
  # create_matches_file('1924/champions-tour-2024-pacific-kickoff')
  # create_matches_file('1925/champions-tour-2024-emea-kickoff')
  # create_matches_file('1926/champions-tour-2024-china-kickoff')
  # create_matches_file('1923/champions-tour-2024-americas-kickoff')
  # create_matches_file('1921/champions-tour-2024-masters-madrid')
  
  # create_matches_file('2002/champions-tour-2024-pacific-stage-1')
  # create_matches_file('1998/champions-tour-2024-emea-stage-1')
  # create_matches_file('2004/champions-tour-2024-americas-stage-1')
  # create_matches_file('2006/champions-tour-2024-china-stage-1')
  # create_matches_file('1999/champions-tour-2024-masters-shanghai')
  
  # create_matches_file('2094/champions-tour-2024-emea-stage-2')
  # create_matches_file('2005/champions-tour-2024-pacific-stage-2')
  # create_matches_file('2096/champions-tour-2024-china-stage-2')
  # create_matches_file('2095/champions-tour-2024-americas-stage-2')
  # create_matches_file('2097/valorant-champions-2024')

  # 2025
  # create_matches_file('2275/vct-2025-china-kickoff')
  # create_matches_file('2274/vct-2025-americas-kickoff')
  # create_matches_file('2277/vct-2025-pacific-kickoff')
  # create_matches_file('2276/vct-2025-emea-kickoff')
  # create_matches_file('2281/valorant-masters-bangkok-2025')

  # create_matches_file('2347/vct-2025-americas-stage-1')
  # create_matches_file('2359/vct-2025-china-stage-1')
  # create_matches_file('2379/vct-2025-pacific-stage-1')
  # create_matches_file('2380/vct-2025-emea-stage-1')
  # create_matches_file('2282/valorant-masters-toronto-2025')

  # create_matches_file('2499/vct-2025-china-stage-2')
  # create_matches_file('2500/vct-2025-pacific-stage-2')
  # create_matches_file('2498/vct-2025-emea-stage-2')
  # create_matches_file('2501/vct-2025-americas-stage-2')
  # create_matches_file('2283/valorant-champions-2025')

# 2026
  # create_matches_file('2682/vct-2026-americas-kickoff')
  # create_matches_file('2683/vct-2026-pacific-kickoff')
  # create_matches_file('2684/vct-2026-emea-kickoff')
  # create_matches_file('2685/vct-2026-china-kickoff')

  # create_matches_file('2760/valorant-masters-santiago-2026')


  # 2021
  # update_match_results('351/champions-tour-korea-stage-1-masters', generate_gif)
  # update_match_results('342/champions-tour-turkey-stage-1-masters', generate_gif)
  # update_match_results('334/champions-tour-europe-stage-1-masters', generate_gif)
  # update_match_results('333/champions-tour-north-america-stage-1-masters', generate_gif)
  # update_match_results('340/champions-tour-latam-stage-1-masters', generate_gif)
  # update_match_results('352/champions-tour-japan-stage-1-masters', generate_gif)
  # update_match_results('347/champions-tour-sea-stage-1-masters', generate_gif)
  # update_match_results('338/champions-tour-brazil-stage-1-masters', generate_gif)

  # update_match_results('441/champions-tour-japan-stage-2-challengers-finals', generate_gif)
  # update_match_results('429/champions-tour-sea-stage-2-challengers-finals', generate_gif)
  # update_match_results('426/champions-tour-korea-stage-2-challengers', generate_gif)
  # update_match_results('376/champions-tour-stage-2-emea-challengers-playoffs', generate_gif)
  # update_match_results('372/champions-tour-north-america-stage-2-challengers-finals', generate_gif)
  # update_match_results('366/champions-tour-brazil-stage-2-challengers-finals', generate_gif)
  # update_match_results('398/champions-tour-latam-stage-2-challengers-finals', generate_gif)
  # update_match_results('353/valorant-champions-tour-stage-2-masters-reykjav-k', generate_gif)

  # update_match_results('540/champions-tour-japan-stage-3-challengers-playoffs', generate_gif)
  # update_match_results('595/champions-tour-korea-stage-3-challengers', generate_gif)
  # update_match_results('578/champions-tour-north-america-stage-3-challengers-playoffs', generate_gif)
  # update_match_results('621/champions-tour-latam-stage-3-challengers-playoffs', generate_gif)
  # update_match_results('547/champions-tour-stage-3-emea-challengers-playoffs', generate_gif)
  # update_match_results('536/champions-tour-brazil-stage-3-challengers-playoffs', generate_gif)
  # update_match_results('570/champions-tour-sea-stage-3-challengers-playoffs', generate_gif)
  # update_match_results('466/valorant-champions-tour-stage-3-masters-berlin', generate_gif)

  # update_match_results('560/champions-tour-asia-pacific-last-chance-qualifier', generate_gif)
  # update_match_results('559/champions-tour-emea-last-chance-qualifier', generate_gif)
  # update_match_results('561/champions-tour-south-america-last-chance-qualifier', generate_gif)
  # update_match_results('558/champions-tour-north-america-last-chance-qualifier', generate_gif)

  # update_match_results('449/valorant-champions-2021', generate_gif)

  # 2022
  # update_match_results('884/champions-tour-asia-pacific-stage-1-challengers-playoffs', generate_gif)
  # update_match_results('850/champions-tour-korea-stage-1-challengers', generate_gif)
  # update_match_results('853/champions-tour-japan-stage-1-challengers-playoffs', generate_gif)
  # update_match_results('854/champions-tour-stage-1-emea-challengers', generate_gif)
  # update_match_results('799/champions-tour-north-america-stage-1-challengers', generate_gif)
  # update_match_results('829/champions-tour-brazil-stage-1-challengers-1', generate_gif)
  # update_match_results('925/champions-tour-latin-america-stage-1-playoffs', generate_gif)
  # update_match_results('948/champions-tour-latam-br-stage-1-last-chance-qualifier', generate_gif)
  # update_match_results('926/valorant-champions-tour-stage-1-masters-reykjav-k', generate_gif)

  # update_match_results('1013/champions-tour-japan-stage-2-challengers-playoffs', generate_gif)
  # update_match_results('998/champions-tour-korea-stage-2-challengers', generate_gif)
  # update_match_results('1063/champions-tour-asia-pacific-stage-2-challengers-playoffs', generate_gif)
  # update_match_results('984/champions-tour-emea-stage-2-challengers', generate_gif)
  # update_match_results('911/champions-tour-brazil-stage-2-challengers', generate_gif)
  # update_match_results('800/champions-tour-north-america-stage-2-challengers', generate_gif)
  # update_match_results('1086/champions-tour-latin-america-stage-2-playoffs', generate_gif)
  # update_match_results('1085/champions-tour-latam-br-stage-2-last-chance-qualifier', generate_gif)
  # update_match_results('1014/valorant-champions-tour-stage-2-masters-copenhagen', generate_gif)

  # update_match_results('1084/champions-tour-asia-pacific-last-chance-qualifier', generate_gif)
  # update_match_results('1130/champions-tour-north-america-last-chance-qualifier', generate_gif)
  # update_match_results('1083/champions-tour-east-asia-last-chance-qualifier', generate_gif)
  # update_match_results('1117/champions-tour-emea-last-chance-qualifier', generate_gif)
  # update_match_results('1111/champions-tour-south-america-last-chance-qualifier', generate_gif)
  # update_match_results('1015/valorant-champions-2022', generate_gif)

  # 2023
  # update_match_results('1188/champions-tour-2023-lock-in-s-o-paulo', generate_gif)

  # update_match_results('1191/champions-tour-2023-pacific-league', generate_gif)
  # update_match_results('1190/champions-tour-2023-emea-league', generate_gif)
  # update_match_results('1189/champions-tour-2023-americas-league', generate_gif)
  # update_match_results('1494/champions-tour-2023-masters-tokyo', generate_gif)

  # update_match_results('1664/champions-tour-2023-champions-china-qualifier', generate_gif)
  # update_match_results('1660/champions-tour-2023-pacific-last-chance-qualifier', generate_gif)
  # update_match_results('1659/champions-tour-2023-emea-last-chance-qualifier', generate_gif)
  # update_match_results('1658/champions-tour-2023-americas-last-chance-qualifier', generate_gif)
  # update_match_results('1657/valorant-champions-2023', generate_gif)

  # 2024
  # update_match_results('1924/champions-tour-2024-pacific-kickoff', generate_gif)
  # update_match_results('1925/champions-tour-2024-emea-kickoff', generate_gif)
  # update_match_results('1926/champions-tour-2024-china-kickoff', generate_gif)
  # update_match_results('1923/champions-tour-2024-americas-kickoff', generate_gif)
  # update_match_results('1921/champions-tour-2024-masters-madrid', generate_gif)
  
  # update_match_results('2002/champions-tour-2024-pacific-stage-1', generate_gif)
  # update_match_results('1998/champions-tour-2024-emea-stage-1', generate_gif)
  # update_match_results('2004/champions-tour-2024-americas-stage-1', generate_gif)
  # update_match_results('2006/champions-tour-2024-china-stage-1', generate_gif)
  # update_match_results('1999/champions-tour-2024-masters-shanghai', generate_gif)
  
  # update_match_results('2094/champions-tour-2024-emea-stage-2', generate_gif)
  # update_match_results('2005/champions-tour-2024-pacific-stage-2', generate_gif)
  # update_match_results('2096/champions-tour-2024-china-stage-2', generate_gif)
  # update_match_results('2095/champions-tour-2024-americas-stage-2', generate_gif)
  # update_match_results('2097/valorant-champions-2024', generate_gif)

  # 2025
  # update_match_results('2275/vct-2025-china-kickoff', generate_gif)
  # update_match_results('2274/vct-2025-americas-kickoff', generate_gif)
  # update_match_results('2277/vct-2025-pacific-kickoff', generate_gif)
  # update_match_results('2276/vct-2025-emea-kickoff', generate_gif)
  # update_match_results('2281/valorant-masters-bangkok-2025', generate_gif)

  # update_match_results('2347/vct-2025-americas-stage-1', generate_gif)
  # update_match_results('2359/vct-2025-china-stage-1', generate_gif)
  # update_match_results('2379/vct-2025-pacific-stage-1', generate_gif)
  # update_match_results('2380/vct-2025-emea-stage-1', generate_gif)
  # update_match_results('2282/valorant-masters-toronto-2025', generate_gif)

  # update_match_results('2499/vct-2025-china-stage-2', generate_gif)
  # update_match_results('2500/vct-2025-pacific-stage-2', generate_gif)
  # update_match_results('2498/vct-2025-emea-stage-2', generate_gif)
  # update_match_results('2501/vct-2025-americas-stage-2', generate_gif)
  # update_match_results('2283/valorant-champions-2025', generate_gif)

  # 2026
  # update_match_results('2682/vct-2026-americas-kickoff', generate_gif)
  # update_match_results('2683/vct-2026-pacific-kickoff', generate_gif)
  # update_match_results('2684/vct-2026-emea-kickoff', generate_gif)
  # update_match_results('2685/vct-2026-china-kickoff', generate_gif)

  
  # update_match_results('2760/valorant-masters-santiago-2026', generate_gif)

  calculate_sos()
  create_table('2026')