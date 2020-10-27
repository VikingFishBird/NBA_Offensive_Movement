import nba_api.stats.static.players as nba_players
from nba_api.stats.endpoints import leaguedashptstats as team_tracking
from nba_api.stats.endpoints import teamestimatedmetrics as team_advanced_stats
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

YEAR = '2019-20'

mpl.rcParams['figure.figsize'] = (8, 5)
plt.style.use('fivethirtyeight')
nba_colors_rgb = {
    'Atlanta Hawks': (225, 68, 52),             # ATL
    'Boston Celtics': (0, 122, 51),             # BOS
    'Brooklyn Nets': (0, 0, 0),                 # BRO
    'Charlotte Hornets': (29, 17, 96),          # CHA
    'Chicago Bulls': (206, 17, 65),             # CHI
    'Cleveland Cavaliers': (134, 0, 56),        # CLE
    'Dallas Mavericks': (0, 83, 188),           # DAL
    'Denver Nuggets': (13, 34, 64),             # DEN
    'Detroit Pistons': (200, 16, 46),           # DET
    'Golden State Warriors': (29, 66, 138),     # GSW
    'Houston Rockets': (206, 17, 65),           # HOU
    'Indiana Pacers': (0, 45, 98),              # IND
    'LA Clippers': (200, 16, 46),               # LAC
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

spectrum_tracking_stats = (
    team_tracking
        .LeagueDashPtStats(season=YEAR, per_mode_simple='PerGame')
        .get_data_frames()[0]
        .get(['TEAM_ID', 'TEAM_NAME', 'TEAM_ABBREVIATION', 'DIST_MILES_OFF', 'AVG_SPEED_OFF'])
)
print(spectrum_tracking_stats.columns)
advanced_stats = (
    team_advanced_stats
        .TeamEstimatedMetrics(season=YEAR)
        .get_data_frames()[0]
        .get(['TEAM_ID', 'E_OFF_RATING', 'E_DEF_RATING', 'E_NET_RATING', 'E_PACE'])
)

print(spectrum_tracking_stats)

merged_team_stats = spectrum_tracking_stats.merge(advanced_stats, left_on='TEAM_ID', right_on='TEAM_ID')
merged_team_stats.set_index('TEAM_ID', inplace=True)

ax = merged_team_stats.plot(x='DIST_MILES_OFF', y='E_OFF_RATING', kind='scatter')
for team_id in merged_team_stats.index:
    plt.scatter(merged_team_stats.get('DIST_MILES_OFF').loc[team_id],
                merged_team_stats.get('E_OFF_RATING').loc[team_id],
                color=nba_colors_normalized[merged_team_stats.get('TEAM_NAME').loc[team_id]])
    plt.text(merged_team_stats.get('DIST_MILES_OFF').loc[team_id],
                merged_team_stats.get('E_OFF_RATING').loc[team_id],
                merged_team_stats.get('TEAM_ABBREVIATION').loc[team_id])

plt.show()

# https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season
# https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/endpoints/leaguedashptstats.md
# https://github.com/swar/nba_api/blob/master/nba_api/stats/endpoints/leaguedashptstats.py
