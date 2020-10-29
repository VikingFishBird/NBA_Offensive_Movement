# An analysis of the top 20 players and
# their offensive movement per request :)

from nba_api.stats.endpoints import leaguedashptstats as player_tracking
from nba_api.stats.endpoints import teamestimatedmetrics as team_advanced_stats
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import unicodedata

# This can be adjusted.
# Works for every season including and after 2013-14
YEAR = '2019-20'

def format_player_name(name):
    new_name = name.split('\\')[0].replace('[', '').replace(']', '')
    return new_name

# remove accents from names for merge of bref and nba.com
def unaccent_name(name):
    new_name = ''.join(c for c in unicodedata.normalize('NFD', name) if unicodedata.category(c) != 'Mn')
    return new_name

# format name as B. Finch
def format_player_name_for_graph(name):
    split_name = name.split(' ')
    new_name = "{}. {}".format(split_name[0][0], split_name[1])
    return new_name

# Configure plot settings
mpl.rcParams['figure.figsize'] = (8, 5)
plt.style.use('ggplot')  # 7, 14
nba_colors_rgb = {
    'Atlanta Hawks': (225, 68, 52),             # ATL
    'Boston Celtics': (0, 122, 51),             # BOS
    'Brooklyn Nets': (0, 0, 0),                 # BRO
    'Charlotte Hornets': (29, 17, 96),          # CHA
    'Charlotte Bobcats': (29, 17, 96),          # CHA
    'Chicago Bulls': (206, 17, 65),             # CHI
    'Cleveland Cavaliers': (134, 0, 56),        # CLE
    'Dallas Mavericks': (0, 83, 188),           # DAL
    'Denver Nuggets': (13, 34, 64),             # DEN
    'Detroit Pistons': (200, 16, 46),           # DET
    'Golden State Warriors': (29, 66, 138),     # GSW
    'Houston Rockets': (206, 17, 65),           # HOU
    'Indiana Pacers': (0, 45, 98),              # IND
    'LA Clippers': (200, 16, 46),               # LAC
    'Los Angeles Clippers': (200, 16, 46),      # LAC
    'Los Angeles Lakers': (85, 37, 130),        # LAL
    'Memphis Grizzlies': (93, 118, 169),        # MEM
    'Miami Heat': (152, 0, 46),                 # MIA
    'Milwaukee Bucks': (0, 71, 27),             # MIL
    'Minnesota Timberwolves': (12, 35, 64),     # MIN
    'New Orleans Pelicans': (0, 22, 65),        # NOP
    'New York Knicks': (0, 107, 182),           # NYK
    'Oklahoma City Thunder': (0, 125, 195),     # OKC
    'Orlando Magic': (0, 125, 197),             # ORL
    'Philadelphia 76ers': (0, 107, 182),        # PHI
    'Phoenix Suns': (29, 17, 96),               # PHO
    'Portland Trail Blazers': (224, 58, 62),    # POR
    'Sacramento Kings': (91, 43, 130),          # SAC
    'San Antonio Spurs': (196, 206, 211),       # SAS
    'Toronto Raptors': (206, 17, 65),           # TOR
    'Utah Jazz': (0, 43, 92),                   # UTA
    'Washington Wizards': (0, 43, 92),          # WAS
}
nba_colors_normalized = {}

# Normalize RGB values to 0-1
for key in nba_colors_rgb:
    nba_colors_normalized[key] = (nba_colors_rgb[key][0]/255, nba_colors_rgb[key][1]/255, nba_colors_rgb[key][2]/255)

# Create dataframe with distance traveled stats
spectrum_tracking_player_stats = (
    player_tracking
        .LeagueDashPtStats(season=YEAR, per_mode_simple='PerGame', player_or_team='Player')
        .get_data_frames()[0]
        .get(['TEAM_ID', 'PLAYER_NAME', 'DIST_MILES_OFF', 'AVG_SPEED_OFF'])
)

spectrum_tracking_player_stats['PLAYER_NAME'] = spectrum_tracking_player_stats.get('PLAYER_NAME').apply(unaccent_name)

# Create dataframe with distance advanced team stats
team_info = (
    team_advanced_stats
        .TeamEstimatedMetrics(season=YEAR)
        .get_data_frames()[0]
        .get(['TEAM_ID', 'TEAM_NAME'])
)
print(spectrum_tracking_player_stats.columns)

# region BREF advanced VORP
bref_vorp = pd.read_csv('data/19-20_nba_vorp.csv')
bref_vorp['Player'] = bref_vorp.get('Player').apply(format_player_name)
bref_vorp.set_index('Rk', inplace=True)
# endregion

top_players_by_vorp = bref_vorp[bref_vorp.get('VORP▼') >= 2.5].get(['Player', 'VORP▼'])
top_players_by_vorp['Player'] = top_players_by_vorp.get('Player').apply(unaccent_name)

merged_player_df = (
    spectrum_tracking_player_stats
        .merge(team_info, left_on='TEAM_ID', right_on='TEAM_ID')
        .merge(top_players_by_vorp, left_on='PLAYER_NAME', right_on='Player')
        .sort_values(by='VORP▼', ascending=False)
)

del merged_player_df['Player']

print(merged_player_df)

# region VORP vs DIST_MILES_OFF
# Label axis: E_OFF_RATING vs DIST_MILES_OFF
vorp_vs_dist = merged_player_df.plot(x='DIST_MILES_OFF', y='VORP▼', kind='scatter')
plt.title('Player VORP vs Distance Traveled ({})'.format(YEAR), fontname='DejaVu Sans', fontsize=18)
plt.xlabel('Distance Traveled on Offense p/g (mi)', fontname='DejaVu Sans', fontsize=14)
plt.ylabel('VORP', fontname='DejaVu Sans', fontsize=14)

# Plot & color: E_OFF_RATING vs DIST_MILES_OFF
for id in merged_player_df.index:
    plt.scatter(merged_player_df.get('DIST_MILES_OFF').loc[id],
                merged_player_df.get('VORP▼').loc[id],
                color=nba_colors_normalized[merged_player_df.get('TEAM_NAME').loc[id]])
    plt.text(merged_player_df.get('DIST_MILES_OFF').loc[id] + 0.005,
                merged_player_df.get('VORP▼').loc[id] + 0.05,
                format_player_name_for_graph(merged_player_df.get('PLAYER_NAME').loc[id]),
                fontname='DejaVu Sans', fontsize=9)
# endregion

# region VORP vs SPEED
# Label axis: E_OFF_RATING vs DIST_MILES_OFF
vorp_vs_spd = merged_player_df.plot(x='AVG_SPEED_OFF', y='VORP▼', kind='scatter')
plt.title('Player VORP vs Average Speed ({})'.format(YEAR), fontname='DejaVu Sans', fontsize=18)
plt.xlabel('Average Speed on Offense (mph)', fontname='DejaVu Sans', fontsize=14)
plt.ylabel('VORP', fontname='DejaVu Sans', fontsize=14)

# Plot & color: E_OFF_RATING vs DIST_MILES_OFF
for id in merged_player_df.index:
    plt.scatter(merged_player_df.get('AVG_SPEED_OFF').loc[id],
                merged_player_df.get('VORP▼').loc[id],
                color=nba_colors_normalized[merged_player_df.get('TEAM_NAME').loc[id]])
    plt.text(merged_player_df.get('AVG_SPEED_OFF').loc[id] + 0.005,
                merged_player_df.get('VORP▼').loc[id] + 0.05,
                format_player_name_for_graph(merged_player_df.get('PLAYER_NAME').loc[id]),
                fontname='DejaVu Sans', fontsize=9)
# endregion

plt.show()
