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
    return type(transcript)
    # trans = transcript[0]['content']
    # date = transcript[0]['date']
    # date_ = str(date).split(' ')[0]
    # return [date_, trans]


print(get_transcript('ALGM', 2020, 3))
