import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests

year = '2019-20'
url = 'https://stats.nba.com/players/speed-distance/?sort=DIST_MILES&dir=1&Season={}&SeasonType=Regular%20Season'.format(year)

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
parsed_table = soup.find_all('table')[0]
print(parsed_table)
