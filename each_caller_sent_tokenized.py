#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


# In[123]:


### Problem, this method does not exclude questions. ###
def get_transcript(ticker, year, quarter,key = '22579006dc377a880ec7abbba96fbdd2'):
    transcript = requests.get(f'https://financialmodelingprep.com/api/v3/earning_call_transcript/{ticker}?quarter={quarter}&year={year}&apikey={key}').json()
    return transcript
    #tran = transcript[0]['content']
    #date = transcript[0]['date']
    #date_ = str(date).split()[0]
    #return [tran, date_]



test_tech = ['AAPL','AMZN']
test_quarters= [1,2,3,4]
test_years = [2019,2020]
call_pull('AAPL', 2020, 1)


# In[82]:


from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize.treebank import TreebankWordDetokenizer
times = [str(f)+':00' for f in range(24)]
times


# In[124]:


apple = get_transcript('AAPL', 2020, 1)
apple


# In[248]:


def get_transcript(ticker, year, quarter):
    key = '22579006dc377a880ec7abbba96fbdd2'
    transcript = requests.get(f'https://financialmodelingprep.com/api/v3/earning_call_transcript/{ticker}?quarter={quarter}&year={year}&apikey={key}').json()
    #tickers = list()
    #years = list()
    #quarter = list()
    #date_list = list()
    date = transcript[0]['date']
    date_ = str(date).split()[0]
    tran = transcript[0]['content']
    
    ref = []
    for line in tran.split('\n'):
        paragraph = sent_tokenize(line)
        for each_sentence in paragraph:
            #tokenized_words = word_tokenize(each_sentence)
            #print([f for f in tokenized_words if f not in times])
            '''
            tickers = list()
            date_list = list()
            names = list()
            sents = list()
            
            if ':' in each_sentence:
                name, rest = each_sentence.split(':')
                
                tickers.append(ticker)
                tickers.append(date_)
                tickers.append(name)
                tickers.append(rest)
                
                #print(ticker, date_, name,  rest)
            else:
                
                tickers.append(ticker)
                tickers.append(date_)
                tickers.append(name)
                tickers.append(each_sentence)
                #print(ticker, date_, name, each_sentence)
            ref.append(tickers)
        
    return pd.DataFrame(ref, columns = ['ticker', 'ognoo', 'name', 'script'])'''

pd.set_option('display.max_rows', None)
get_transcript('AAPL', 2020, 1)


# In[ ]:


def better_entire_report_pull(stock_list, year_list, quarter_list):
    report = []
    for stock in stock_list:
        for yr in year_list:
            for qtr in quarter_list:
                stonks = []
                stonks.append(stock)
#                 stonks.append(f'{yr}')
                try:
                    trans, date = call_pull(stock, yr, qtr)
                    stonks.append(trans)
                    stonks.append(date)
                except:
                    stonks.append(np.nan)
                    stonks.append(np.nan)
                report.append(stonks)
    return pd.DataFrame(report, columns = ['Ticker','Transcript', 'Date'])


# In[224]:


for line in apple.split('\n'):
    paragraph = sent_tokenize(line)
    for each_sentence in paragraph:
        print(each_sentence)


# In[185]:


import csv
csv.writer(a)


# In[215]:


import docx
from docx import Document
Document(apple)


# In[42]:


times = [str(f)+':00' for f in range(24)]


# In[29]:


def better_entire_report_pull(stock_list, year_list, quarter_list):
    report = []
    for stock in stock_list:
        for yr in year_list:
            for qtr in quarter_list:
                stonks = []
                stonks.append(stock)
#                 stonks.append(f'{yr}')
                try:
                    trans, date = call_pull(stock, yr, qtr)
                    stonks.append(trans)
                    stonks.append(date)
                except:
                    stonks.append(np.nan)
                    stonks.append(np.nan)
                report.append(stonks)
    return pd.DataFrame(report, columns = ['Ticker','Transcript', 'Date'])


# In[31]:


X = better_entire_report_pull(test_tech, [2017, 2018, 2019, 2020], [1,2,3,4])

X = X.dropna(axis=0)
X.head()


# In[36]:


def yfin(df):
    
    for index, row in df.iterrows():
        
        ticker = row['Ticker']
        date = datetime.strptime(row['Date'], '%Y-%m-%d')
        return [ticker, date]
        date_90 = date + timedelta(days=90)
        #return [ticker, date, date_90]
        
        try:
            data = yf.download(ticker, start=date, end=date_90, interval = '3mo')
            VGT = yf.download('VGT', start=date, end=date_90, interval = '3mo')
        
            adj = data['Adj Close'][0]
            adj_1 = data['Adj Close'][-1]
            percent_change = adj_1/adj -1
    
            VGTadj = VGT['Adj Close'][0]
            VGTadj_1 = VGT['Adj Close'][-1]
            VGTpercent_change = VGTadj_1/VGTadj -1
        except:
            percent_change = np.nan
            VGTpercent_change= np.nan

    
        return [percent_change, VGTpercent_change]
    
yfin(X)


# In[14]:


X
#X['ticker_data'] = X.apply(yfin, axis=1)


# In[13]:


#X


# In[159]:


import textstat
help(textstat)

