import pandas as pd
##Reading file
from pandas.conftest import axis

df = pd.read_csv(r"C:\Users\user\Downloads\Datasets\Monthly Crude Oil Production by State 1981 - Nov 2016.csv")
print(df)
print(df.columns)
#Renaming columns
Rename = df.rename(columns={'East Coast (PADD 1) Field Production of Crude Oil (Thousand Barrels)': 'EC (PADD 1)'})
print(Rename)
import hypothesis as hp

df.columns=('Date', 'U.S. Field Production', 'East Coast (PADD 1)', 'Florida Field Production ',
       'New York Field Production ',
       'Pennsylvania Field Production',
       'Virginia Field Production',
       'West Virginia Field Production',
       'Midwest (PADD 2) Field Production',
       'Illinois Field Production',
       'Indiana Field Production ',
       'Kansas Field Production',
       'Kentucky Field Production',
       'Michigan Field Production',
       'Missouri Field Production',
       'Nebraska Field Production',
       'North Dakota Field Production',
       'Ohio Field Production ',
       'Oklahoma Field Production ',
       'South Dakota Field Production ',
       'Tennessee Field Production',
       'Gulf Coast (PADD 3) Field Production',
       'Alabama Field Production',
       'Arkansas Field Production',
       'Louisiana Field Production',
       'Mississippi Field Production',
       'New Mexico Field Production ',
       'Texas Field Production',
       'Federal Offshore--Gulf of Mexico Field Production',
       'Rocky Mountain (PADD 4) Field Production',
       'Colorado Field Production',
       'Montana Field Production',
       'Utah Field Production',
       'Wyoming Field Production',
       'West Coast (PADD 5) Field Production',
       'Alaska Field Production',
       'Alaska South Field Production',
       'Alaska North Slope Production',
       'Arizona Field Production',
       'California Field Production',
       'Nevada Field Production',
       'Federal Offshore PADD 5 Field Production', 'Unnamed: 42',)
print(df.columns)
##Plotting East Coast (PADD 1) against the years of production

##aggregating East Coast (PADD 1)
df_agg = df.groupby('Date').agg([sum])
print(df_agg)
#creating plot figure
import pyplot as plt

df_fig = plt.figure
ax.plot(df['Date'], df[df.column[2]])
plt.show