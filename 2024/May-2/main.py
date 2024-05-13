"""
    Makeover Monday submission for the prompt from 13-May-2024
    
    Created 05-13-24
"""

import polars as pl
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import numpy as np
from os import path

# Import .csv file

filename = 'gun_exports.csv'
filepath = path.join('/home/cdoss/work/mm/2024/May-2', filename)

# Load a dataframe, then filter a subset to represent the top 10 in rank

df = pl.read_csv(filepath)

top = df.filter(
    pl.col('Rank') < 6
)

for country in df['Country']:
    print(country)

# Create a dictionary to represent countries by their respective regions

region = {
    'East Asia': [
        'Thailand'
        ],
    'Middle East': [
        'Saudi Arabia',
        'Israel',
        'United Arab Emirates',
        ],
    'Eastern Europe': [
        'Czech Republic',
        ],
    'Western Europe': [
        'Belgium',
        'Italy',
        'Germany',
        'France',
        'Switzerland',
        
        ],
    'North/Central America': [
        'Canada',
        'Mexico',
        'Guatemala',
        ],
    'South America': [
        'Brazil',
        ],
    'Oceania': [
        'Philippines',
        'Australia',
        ],
    'North Africa': [
        
        ],
    'Sub-Saharan Africa': [
        'South Africa',
        ],
    'West Africa': [
        
        ],
}

# Styling and forming the plots with matplotlib and pyplot

plt.style.use('/home/cdoss/work/btl/btl.mplstyle')

fig, ax1 = plt.subplots(1, 1)

ax1.bar(top['Country'], top['Cumulative Volume'])

plt.show()