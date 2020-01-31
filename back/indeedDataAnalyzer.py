"""
component to analyze the data scraped from indeed
Calculates thing like mean, standard deviation, and zscore
"""
import pandas as pd
import numpy as np
import math


#from back.indeedScraper import totalJobsDictionary

#create an array of strings for the dataframe row labels
row_labels = ['TotalJobs', 'Zscore']


#analyze the data scraped from the indeed website and calculate various statistics on items
#IN: the dictionary containing state/totaljob pairs from the indeed scraper
#OUT: a PANDAS dataframe containing the states and their total jobs as well as the z-score comparing it to the mean
def analyzeIndeedData(totalJobsDictionary):
    #turn the dictionary into a PANDAS dataframe and calculate the mean and standard deviation
    df = pd.DataFrame(data=[totalJobsDictionary])
    mean = df.mean(axis = 1)[0]
    std = df.std(axis = 1)[0]
    #calculate the zscores and append them to the data frame for each of their respective state abbreviations
    zscores = pd.Series((df.iloc[0] - mean) / std)
    df.loc[len(df)] = zscores
    df.index = row_labels
    
    return df
