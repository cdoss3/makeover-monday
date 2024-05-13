"""
    Makeover Monday submission for the prompt from 13-May-2024
    
    Created 05-13-24
    
    Notes on region selection:
        - There were a few countries which were placed in regions by myself.
        I am not an expert on geography, and in the event you disagree with 
        the region of a country, that's fair.
        - Cyprus was placed in Eastern Europe because its culture is closer
        to Eastern Europe than it is the Middle East.
        - Netherlands Antilles might get tricky if we zoom in on the countries
        individually, but it should be OK since we're grouping by region
        - If a country was on the border of two regions, I tried to place them
        with the region it would tie more closely with culturally. I used 
        the country's dominant religion as the litmus test

"""

import polars as pl
from matplotlib import pyplot as plt
from os import path

# Import .csv file

filename = 'gun_exports.csv'
filepath = path.join('/home/cdoss/work/mm/2024/May-2', filename)

# Load a dataframe, then filter a subset to represent the top 5 in rank

df = pl.read_csv(filepath)

top = df.filter(
    pl.col('Rank') < 6
)

for country in df['Country']:
    print(country)

# Create a dictionary to represent countries by their respective regions
#
# LAST COUNTRY PLACED - CYPRUS

region = {
    'East Asia': [
        'Thailand',
        'India',
        'Pakistan',
        'Bangladesh',
        'Japan',
        'Taiwan',
        'Singapore',
        'South Korea',
        'North Korea',
        'Vietnam',
        'Cambodia',
        'Sri Lanka',
        'Hong Kong',
        'Laos',
        'Mongolia',
        'Bhutan',
        'China',
        ],
    'Middle East': [
        'Saudi Arabia',
        'Israel',
        'United Arab Emirates',
        'Lebanon',
        'Afghanistan',
        'Oman',
        'Iraq',
        'Jordan',
        'Kuwait',
        'Kazakhstan',
        'Bahrain',
        'Yemen',
        'Kyrgyzstan',
        'Qatar',
        'Uzbekistan',
        'Tajikistan',
        ],
    'Eastern Europe & Scandinavia': [
        'Czech Republic',
        'Turkey',
        'Ukraine',
        'Poland',
        'Georgia',
        'Austria',
        'Finland',
        'Kosovo',
        'Slovakia',
        'Bulgaria',
        'Serbia',
        'Russia',
        'Greece',
        'Armenia',
        'Latvia',
        'Hungary',
        'Lithuania',
        'Estonia',
        'Bosnia and Herzegovina',
        'Moldova',
        'Slovenia',
        'Romania',
        'Macedonia',
        'Albania',
        'Croatia',
        'Montenegro',
        'Azerbaijan',
        'Cyprus'
        ],
    'Western Europe': [
        'Belgium',
        'Italy',
        'Germany',
        'France',
        'Switzerland',
        'Spain',
        'United Kingdom',
        'Portugal',
        'Netherlands',
        'Malta',
        'Ireland',
        'Luxembourg',
        'Greenland',
        'Iceland',
        'Vatican City',
        'Andorra',
        ],

    'North/Central America': [
        'Canada',
        'Mexico',
        'Guatemala',
        'El Salvador',
        'Honduras',
        'Panama',
        'Nicaragua',
        'Belize',
        ],
    'Carribbean': [
        'Costa Rica',
        'Jamaica',
        'Trinidad and Tobago',
        'Dominican Republic',
        'Bahamas',
        'Haiti',
        'Antigua and Barbuda',
        'St Kitts and Nevis',
        'Barbados',
        'St Vincent and the Grenadines',
        'St Lucia',
        'Cayman Islands',
        'Grenada',
        'Aruba',
        'Turks and Caicos Islands',
        'Bermuda',
        'Dominica',
        'Curacao',
        'British Virgin Islands',
        'Anguilla',
        'Netherlands Antilles (through Apr 2011)'
        'St Helena',
        ],
    'South America': [
        'Brazil',
        'Peru',
        'Paraguay',
        'Uruguay',
        'Colombia',
        'Argentina',
        'Chile',
        'Bolivia',
        'Suriname',
        'Guyana',
        'Ecuador',
        'Venezuela',
        ],
    'Oceania': [
        'Philippines',
        'Australia',
        'Indonesia',
        'New Zealand',
        'Malaysia',
        'New Caledonia',
        'Timor-Leste',
        'Papua New Guinea',
        'Fiji',
        'French Polynesia',
        'Mauritius',
        'Kiribati',
        ],
    'North Africa': [
        'Tunisia',
        'Egypt',
        'Morocco',
        'Djibouti',
        'Chad',
        ],
    'Sub-Saharan Africa': [
        'South Africa',
        'Namibia',
        'Kenya',
        'Zambia',
        'Tanzania',
        'Uganda',
        'Cameroon',
        'Somalia',
        'Botswana',
        'South Sudan',
        'Eswatini',
        'Congo (Kinshasa)',
        'Malawi',
        'Angola',
        'Zimbabwe',
        'Mozambique',
        'Central African Republic',
        'Ethiopia',
        ],
    'West Africa': [
        "Cote d'Ivoire",
        'Senegal',
        'Nigeria',
        'Ghana',
        'Niger',
        'Liberia',
        'Mauritania',
        'Mali',
        'Burkina Faso',
        ],
}

# Styling and forming the plots with matplotlib and pyplot
# Style

plt.style.use('/home/cdoss/work/btl/btl.mplstyle')

# Instantiate the figure and axes for multiple subplots

fig, (ax1, ax2) = plt.subplots(1, 2)

# Bar chart - axes 1
ax1.bar(top['Country'], top['Cumulative Volume'])

# Scatter plot - axes 2
ax2.plot(top['Country'], top['Cumulative Volume'])

# Generate the plots
plt.show()