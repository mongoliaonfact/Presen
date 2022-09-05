import pandas as pd
import numpy as np
import yfinance as yfin
import certifi
import json
import ssl
import requests

from datetime import datetime, timedelta


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
                #                 stonks.append(f'{yr}')
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
    return lists


test_tech = ['AAPL', 'AMZN']
test_quarters= [1, 2, 3, 4]
test_years = [2017, 2018, 2019, 2020]

scripts = get_all_transcripts(test_tech, test_years, test_quarters)
#print(scripts)
ticker_data = calcul_data(scripts)
scripts.loc[:, 'ticker_data'] = ticker_data

print(scripts.loc[:, ['ticker', 'ognoo', 'ticker_data']].dropna())
