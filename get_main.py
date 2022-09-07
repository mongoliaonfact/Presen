# @author: bbaasan
# date: 9/6/2022
# bbaasan@gmu.edu

import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import textstat
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, train_test_split, GridSearchCV, KFold
from sklearn.metrics import confusion_matrix, average_precision_score, recall_score, precision_score,log_loss, make_scorer, roc_curve, plot_roc_curve, precision_score, auc
plt.style.use('ggplot')

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from nltk.tokenize import RegexpTokenizer

