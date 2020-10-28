from nba_api.stats.endpoints import leaguedashptstats as team_tracking
from nba_api.stats.endpoints import teamestimatedmetrics as team_advanced_stats
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

# This can be adjusted.
# Works for every season including and after 2013-14
YEAR = '2019-20'

def format_player_name(name):
    new_name = name.split('\\')[0].replace('[', '').replace(']', '')
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
spectrum_tracking_stats = (
    team_tracking
        .LeagueDashPtStats(season=YEAR, per_mode_simple='PerGame')
        .get_data_frames()[0]
        .get(['TEAM_ID', 'TEAM_NAME', 'TEAM_ABBREVIATION', 'DIST_MILES_OFF', 'AVG_SPEED_OFF'])
)

# Create dataframe with distance advanced team stats
advanced_stats = (
    team_advanced_stats
        .TeamEstimatedMetrics(season=YEAR)
        .get_data_frames()[0]
        .get(['TEAM_ID', 'E_OFF_RATING', 'E_DEF_RATING', 'E_NET_RATING', 'E_PACE'])
)

# Merge tables
merged_team_stats = spectrum_tracking_stats.merge(advanced_stats, left_on='TEAM_ID', right_on='TEAM_ID')
merged_team_stats.set_index('TEAM_ID', inplace=True)

# region E_OFF_RATING vs DIST_MILES_OFF
# Label axis: E_OFF_RATING vs DIST_MILES_OFF
dist_vs_orat = merged_team_stats.plot(x='DIST_MILES_OFF', y='E_OFF_RATING', kind='scatter')
plt.title('Offensive Rating vs Distance Traveled ({})'.format(YEAR), fontname='DejaVu Sans', fontsize=18)
plt.xlabel('Distance Traveled on Offense p/g (mi)', fontname='DejaVu Sans', fontsize=14)
plt.ylabel('Offensive Rating', fontname='DejaVu Sans', fontsize=14)

# Plot & color: E_OFF_RATING vs DIST_MILES_OFF
for team_id in merged_team_stats.index:
    plt.scatter(merged_team_stats.get('DIST_MILES_OFF').loc[team_id],
                merged_team_stats.get('E_OFF_RATING').loc[team_id],
                color=nba_colors_normalized[merged_team_stats.get('TEAM_NAME').loc[team_id]])
    plt.text(merged_team_stats.get('DIST_MILES_OFF').loc[team_id] + 0.01,
                merged_team_stats.get('E_OFF_RATING').loc[team_id] + 0.1,
                merged_team_stats.get('TEAM_ABBREVIATION').loc[team_id],
                fontname='DejaVu Sans', fontsize=9)
# endregion

# region E_OFF_RATING vs AVG_SPEED_OFF
# Label axis: E_OFF_RATING vs AVG_SPEED_OFF
merged_team_stats.plot(x='AVG_SPEED_OFF', y='E_OFF_RATING', kind='scatter')
plt.title('Offensive Rating vs Average Speed ({})'.format(YEAR), fontname='DejaVu Sans', fontsize=18)
plt.xlabel('Average player speed on Offense (mi/h)', fontname='DejaVu Sans', fontsize=14)
plt.ylabel('Offensive Rating', fontname='DejaVu Sans', fontsize=14)

# Plot & color: E_OFF_RATING vs AVG_SPEED_OFF
for team_id in merged_team_stats.index:
    plt.scatter(merged_team_stats.get('AVG_SPEED_OFF').loc[team_id],
                merged_team_stats.get('E_OFF_RATING').loc[team_id],
                color=nba_colors_normalized[merged_team_stats.get('TEAM_NAME').loc[team_id]])
    plt.text(merged_team_stats.get('AVG_SPEED_OFF').loc[team_id] + 0.005,
                merged_team_stats.get('E_OFF_RATING').loc[team_id] + 0.1,
                merged_team_stats.get('TEAM_ABBREVIATION').loc[team_id],
                fontname='DejaVu Sans', fontsize=9)
# endregion

# region DIST_MILES_OFF vs AVG_SPEED_OFF
# Label axis: DIST_MILES_OFF vs AVG_SPEED_OFF
merged_team_stats.plot(x='AVG_SPEED_OFF', y='DIST_MILES_OFF', kind='scatter')
plt.title('Distance Traveled vs Player Speed ({})'.format(YEAR), fontname='DejaVu Sans', fontsize=18)
plt.xlabel('Average player speed on Offense (mi/h)', fontname='DejaVu Sans', fontsize=14)
plt.ylabel('Distance Traveled on Offense p/g (mi)', fontname='DejaVu Sans', fontsize=14)

dist_vs_spd_fit_line = np.poly1d(np.polyfit(merged_team_stats.get('AVG_SPEED_OFF'), merged_team_stats.get('DIST_MILES_OFF'), 1))
line_values = np.linspace(merged_team_stats.get('AVG_SPEED_OFF').min(), merged_team_stats.get('AVG_SPEED_OFF').max(), 100)
plt.plot(line_values, dist_vs_spd_fit_line(line_values), color='grey')

# Plot & color: DIST_MILES_OFF vs AVG_SPEED_OFF
for team_id in merged_team_stats.index:
    plt.scatter(merged_team_stats.get('AVG_SPEED_OFF').loc[team_id],
                merged_team_stats.get('DIST_MILES_OFF').loc[team_id],
                color=nba_colors_normalized[merged_team_stats.get('TEAM_NAME').loc[team_id]])
    plt.text(merged_team_stats.get('AVG_SPEED_OFF').loc[team_id] + 0.005,
                merged_team_stats.get('DIST_MILES_OFF').loc[team_id] + 0.01,
                merged_team_stats.get('TEAM_ABBREVIATION').loc[team_id],
                fontname='DejaVu Sans', fontsize=9)
# endregion

# region Pace vs Deviation from Best Fit
merged_team_stats['Deviation_From_Best_Fit'] = merged_team_stats.get('AVG_SPEED_OFF').apply(dist_vs_spd_fit_line) - merged_team_stats.get('DIST_MILES_OFF')

sorted_by_deviation = merged_team_stats.sort_values(by='Deviation_From_Best_Fit')
deviation_colors = []
for i in range(len(sorted_by_deviation.index)):
    deviation_colors.append(nba_colors_normalized[sorted_by_deviation.get('TEAM_NAME').iloc[i]])

sorted_by_deviation.plot(x='TEAM_ABBREVIATION', y='Deviation_From_Best_Fit', kind='bar', color=deviation_colors)
plt.title('Each Team\'s Deviation from the regression line.'.format(YEAR), fontname='DejaVu Sans', fontsize=18)
plt.xlabel('Team', fontname='DejaVu Sans', fontsize=14)
plt.ylabel('Deviation from the regression line', fontname='DejaVu Sans', fontsize=14)


sorted_by_pace = merged_team_stats.sort_values(by='E_PACE')
pace_colors = []
for i in range(len(sorted_by_pace.index)):
    pace_colors.append(nba_colors_normalized[sorted_by_pace.get('TEAM_NAME').iloc[i]])

sorted_by_pace.plot(x='TEAM_ABBREVIATION', y='E_PACE', kind='bar', color=pace_colors)
plt.title('Each Team\'s Pace ({})'.format(YEAR), fontname='DejaVu Sans', fontsize=18)
plt.xlabel('Team', fontname='DejaVu Sans', fontsize=14)
plt.ylabel('Pace', fontname='DejaVu Sans', fontsize=14)
plt.ylim(sorted_by_pace.get('E_PACE').min() - 1, sorted_by_pace.get('E_PACE').max() + 1)

# Further Comparisons w/ Pace and the deviation
pace_vs_deviation_df = merged_team_stats.get(['TEAM_NAME', 'E_PACE', 'Deviation_From_Best_Fit']).sort_values(by='E_PACE', ascending=False)
pace_vs_deviation_df['Pace_Rank'] = np.arange(1, 31)
pace_vs_deviation_df = pace_vs_deviation_df.sort_values(by='Deviation_From_Best_Fit', ascending=False)
pace_vs_deviation_df['Deviation_Rank'] = np.arange(1, 31)
pace_vs_deviation_df['Avg_Rank'] = (pace_vs_deviation_df['Deviation_Rank'] + pace_vs_deviation_df['Pace_Rank'])/2
pace_vs_deviation_df = pace_vs_deviation_df.sort_values(by='Avg_Rank', ascending=True)

print(pace_vs_deviation_df.get(['TEAM_NAME', 'Pace_Rank', 'Deviation_Rank', 'Avg_Rank']))
# endregion

# region BREF advanced player stats
if YEAR == '2019-20':
    bref_advanced_player_stats = pd.read_csv('data/nba_advanced_player_stats_bref.csv')
    bref_advanced_player_stats['Player'] = bref_advanced_player_stats.get('Player').apply(format_player_name)
    bref_advanced_player_stats.set_index('Rk', inplace=True)
    print(bref_advanced_player_stats)
# endregion

plt.figure(3)
plt.show()
