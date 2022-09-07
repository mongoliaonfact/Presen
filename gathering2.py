# @author: bbaasan
# date: 9/6/2022
# bbaasan@gmu.edu

# @author: bbaasan
# date: 9/5/2022
# bbaasan@gmu.edu
import pandas as pd
import numpy as np
import yfinance as yfin
import certifi
import json
import ssl
import requests
import warnings

warnings.filterwarnings('ignore')

from datetime import datetime, timedelta

def main(stock_list, year_list, quarter_list):


    def get_transcript(ticker, year, quarter):
        key = '22579006dc377a880ec7abbba96fbdd2'
        transcript = requests.get(
            f'https://financialmodelingprep.com/api/v3/earning_call_transcript/{ticker}?quarter={quarter}&year={year}&apikey={key}').json()
        if len(transcript) > 0:
            trans = transcript[0]['content']
            date = transcript[0]['date']
            date_ = str(date).split(' ')[0]
            return [date_, trans]
        else:
            return 'transcript is empty.'


    def get_all_transcripts(stock_list, year_list, quarter_list):
        report = []
        for stock in stock_list:
            for yr in year_list:
                for qtr in quarter_list:
                    stonks = []
                    stonks.append(stock)
                    try:

                        trans, date = get_transcript(stock, yr, qtr)
                        stonks.append(trans)
                        stonks.append(date)
                    except:
                        stonks.append(np.nan)
                        stonks.append(np.nan)
                    report.append(stonks)
        return pd.DataFrame(report, columns=['ticker', 'ognoo', 'transcript'])


    def calcul_data(df):
        lists = list()
        df = df.dropna()

        for index, row in df.iterrows():
            ticker = row['ticker']
            odor = datetime.strptime(row['ognoo'], '%Y-%m-%d')
            days_later_90 = odor + timedelta(days=90)
            try:
                data = yfin.download(ticker, start=odor, end=days_later_90,
                                     interval='3mo')
                vgt = yfin.download('VGT', start=odor, end=days_later_90,
                                    interval='3mo')

                adj = data['Adj Close'][0]
                adj_1 = data['Adj Close'][-1]
                sample_delta = adj_1 / adj - 1

                vgt_adj = vgt['Adj Close'][0]
                vgt_adj_1 = vgt['Adj Close'][-1]
                vgt_delta = vgt_adj_1 / vgt_adj - 1
                lists.append([sample_delta, vgt_delta])
            except:
                sample_delta = np.nan
                vgt_delta = np.nan
                lists.append([sample_delta, vgt_delta])
        df.loc[:, 'ticker_data'] = lists
        return df


    # test_tech = ['AAPL', 'AMZN']

    test_tech = ['ACIW', 'ACLS', 'AGYS', 'ALRM', 'AAPL', 'AMZN']
    test_quarters = [1, 2, 3, 4]
    test_years = [2017, 2018, 2019, 2020]

    scripts = get_all_transcripts(test_tech, test_years, test_quarters)
    # print(scripts)
    scripts = calcul_data(scripts)

    scripts.loc[:, 'VGT'] = scripts['ticker_data'].apply(lambda x: x[1])
    scripts.loc[:, 'sample'] = scripts['ticker_data'].apply(lambda x: x[0])


    def better_than_vgt(scripts, col1, col2):
        ref = list()
        for index, row in scripts.iterrows():
            if row[col1] < row[col2]:
                ref.append(int(1))
            else:
                ref.append(int(0))
        scripts.loc[:, 'better_than_vgt'] = ref
        return scripts

    #print(scripts.head())
    scripts = better_than_vgt(scripts, 'VGT', 'sample')

    return scripts

if __name__ == '__main__':

    # test_tech = ['AAPL', 'AMZN']

    test_tech = ['ACIW', 'ACLS', 'AGYS', 'ALRM', 'AAPL', 'AMZN']
    test_quarters = [1, 2, 3, 4]
    test_years = [2017, 2018, 2019, 2020]
    main(['AAPL', 'AMZN'], [2019, 2020], [1, 2] )