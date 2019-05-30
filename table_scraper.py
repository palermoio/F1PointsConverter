'''
File: table_scraper.py
By: Francesco Palermo
Description: Reads results from f1-fansite.com and stores them as .csv files. Used by points_converter.py to score
seasons.
'''

import pandas as pd
import requests


for year in range(1950,2019):   #get results from all F1 seasons
    url = 'https://www.f1-fansite.com/f1-results/' + str(year) + '-f1-championship-standings/'

    header = {
      "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
      "X-Requested-With": "XMLHttpRequest"
    }

    r = requests.get(url, headers=header)
    dfs = pd.read_html(r.text)

    path = 'D:\\Documents\\F1 Points Conversion\\results\\' + str(year) + '.csv'

    export_csv = dfs[1].iloc[:, 1:-1].to_csv(path, index = None, header=False)