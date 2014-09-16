
# coding: utf-8

# In[4]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[5]:

# For a given feature, split comma-separated values into separate columns and store it in a DataFrame.
def split_feature(feature_list, df, x, length):
    for y in range (0, length):
        if feature_list[y]:
            df.iloc[x,y] = feature_list[y].strip()
        else:
            break
    
    return df


# In[6]:

# Load datasets from Silk - Y Combinator.
startup = pd.DataFrame()
startup = pd.read_csv('Startups.csv')


# In[7]:

# Renaming some column headings for easier reference.
startup.rename(columns={'Satus':'Fate',
                        'Categories':'Market',
                        'Y Combinator Year':'YCYear',
                        'Y Combinator Session':'YCSession',
                        'Amounts raised in different funding rounds':'TotalFunds',
                        'Headquarters (City)':'City',
                        'Seed-DB / Mattermark Profile':'SeedDBMattermarkProfile',
                        'Crunchbase / Angel List Profile':'CrunchBaseAngelListProfile'}, inplace=True)


# In[8]:

# Deleting less predictive features. Mostly because they're redundant, but may revisit in future projects.
startup = startup.drop(['Year Founded',
                        'Office Address',
                        'Mapping Location',
                        'Headquarters (US State)',
                        'Headquarters (Country)'], 1)


# In[9]:

# Some features came with values that are delimited by commas--and they need to be split (for scikit-learn purposes).
# Side note: There is a bit of redundancy, as well as some hard-coded stuff in this block of code.
# I'll figure out a way to clean this up after my demo. 

# Startups tend to identify themselves across many markets.
# For ROI purposes, boiling this feature down to just five.
market = pd.DataFrame(index=range(len(startup)), 
                      columns=['Market1', 'Market2', 'Market3', 'Market4', 'Market5'])
market = market.fillna(NaN)

# Four founders seems like a good common denominator, though there are startups with more founders (but not many).
founders = pd.DataFrame(index=range(len(startup)), 
                      columns=['Founders1', 'Founders2', 'Founders3', 'Founders4'])
founders = founders.fillna(NaN)

# Again, four seems like a good common denominator for investors.
investors = pd.DataFrame(index=range(len(startup)), 
                      columns=['Investors1', 'Investors2', 'Investors3', 'Investors4'])
investors = investors.fillna(NaN)

for index, row in startup.iterrows():
    
    # Drop all stealth companies then skip to the next row.
    if 'Stealth' in row['Company']:
        startup = startup.drop(index)
        continue
    
    # Split up market, founders, and investors.
    if isinstance(row['Market'], basestring):
        marketlist = row['Market'].split(',')
        if len(marketlist) <= 5:            
            market = split_feature(marketlist, market, index, len(marketlist))
        else:
            market = split_feature(marketlist, market, index, 5)
            
    if isinstance(row['Founders'], basestring):
        founderslist = row['Founders'].split(',')
        if len(founderslist) <= 4:            
            founders = split_feature(founderslist, founders, index, len(founderslist))
        else:
            founders = split_feature(founderslist, founders, index, 4)
    
    if isinstance(row['Investors'], basestring):
        investorslist = row['Investors'].split(',')
        if len(investorslist) <= 4:            
            investors = split_feature(investorslist, investors, index, len(investorslist))
        else:
            investors = split_feature(investorslist, investors, index, 4)
    
    # Sum all fundings rounds into a single value.
    if isinstance(row['TotalFunds'], basestring):
        totalfundslist = row['TotalFunds'].split(', ')
        total = 0
        for fund in range(0, len(totalfundslist)):
            if totalfundslist[fund] != 'undisclosed amount':
                totalfundslist[fund] = totalfundslist[fund].replace('$','')
                totalfundslist[fund] = totalfundslist[fund].replace(',','')
                total += int(float(totalfundslist[fund]))
                
        startup.loc[index,['TotalFunds']] = total
        
# Just a reminder to reindex later.


# In[ ]:

# This is good for now. Work on joining DataFrame later. Focus on Hacker News Algolia API.

