import numpy as np
from matplotlib import pyplot as plt

print(np.__version__)


import os
OIL_FILE = r"C:\Users\user\Downloads\Datasets\Monthly Crude Oil Production by State 1981 - Nov 2016.csv"
os.environ['OIL FILE'] =r"C:\Users\user\Downloads\Datasets\Monthly Crude Oil Production by State 1981 - Nov 2016.csv"
print(os.environ)

import pandas as pd
df=pd.read_csv(r"C:\Users\user\Downloads\Datasets\Monthly Crude Oil Production by State 1981 - Nov 2016.csv")
print(df)

print(df.info())

##Renaming all Columns

df.columns=('Date', 'U.S. Field Prod', 'East Coast (PADD 1)', 'Florida Field Prod ',
       'New York Field Prod ',
       'Pennsylvania Field Prod',
       'Virginia Field Prod',
       'West Virginia Field Prod',
       'Midwest (PADD 2) Field Prod',
       'Illinois Field Prod',
       'Indiana Field Prod ',
       'Kansas Field Prod',
       'Kentucky Field Prod',
       'Michigan Field Prod',
       'Missouri Field Prod',
       'Nebraska Field Prod',
       'North Dakota Field Prod',
       'Ohio Field Prod ',
       'Oklahoma Field Prod ',
       'South Dakota Field Prod ',
       'Tennessee Field Prod',
       'GC (PADD 3) Field Prod',
       'Alabama F Prod',
       'Arkansas Field Prod',
       'Louisiana Field Prod',
       'Mississippi Field Prod',
       'New Mexico F Prod ',
       'Texas Field Prod',
       'Federal Offshore--GOM Field Prod',
       'Rocky Mountain (PADD 4) Field Prod',
       'Colorado Field Prod',
       'Montana Field Prod',
       'Utah Field Prod',
       'Wyoming Field Prod',
       'West Coast (PADD 5) Field Prod',
       'Alaska Field Prod',
       'Alaska South Field Prod',
       'Alaska North Slope Prod',
       'Arizona Field Prod',
       'California Field Prod',
       'Nevada Field Prod',
       'Federal Offshore PADD 5 Field Prod',)

print(df.columns)
##Converting Dates
import datetime

df['Date'] =pd.to_datetime(df['Date'],errors="coerce", format="%b-%y",dayfirst=True,)
print(df)

df['Year'] =df['Date'].dt.year

##Converting all data in columns to integers with the exception of the Date column
for col in df.columns[1:]:
    df[col]= pd.to_numeric(df[col])

    print(df.info())

###aggregating years in Date column
df_agg = df.groupby(['Date'], as_index=False).sum()
print(df_agg)

##converting date to string
df_agg['Year'] = df_agg['Date'].astype("str")
print(df_agg['Date'])

##Summing other colums
df_agg=df.agg('sum', axis='columns')
print(df_agg)

import matplotlib.pyplot as plt
fig, axes  = plt.subplots(nrows=3, ncols=3)
plt.show()

axes[0, 1].bar(df[df_agg.columns[0]], df[df_agg.columns[2]])
axes[0, 1].set_title(f"Bar graph of  of US fields. {df.columns[2][:30]}")
axes[1, 1].plot(df[df_agg.columns[0]], df[df_agg.columns[2]], color="green")
##setting axes name
axes[0,1].set_xtitle(f"Year")
plt.show()

for i, ax in enumerate(axes.flat):
    if i == 0:
        ax.bar(df[df_agg.columns[0]], df[df_agg.columns[2]])
        ax.set(title=f" {df_agg.columns[2]}")
    elif i==1:
        ax.bar(df[df_agg.columns[0]], df[df_agg.columns[3]])
        ax.set(title=f" {df_agg.columns[2]}")
    elif i == 2:
        ax.plot(df[df_agg.columns[0]], df[df_agg.columns[4]])
        ax.set(title= f" {df_agg.columns[4]}")
    elif i == 3:
        ax.scatter(df[df_agg.columns[2]], df[df_agg.columns[5]])
        ax.set(title=f" {df_agg.columns[5]}")
plt.title("Oil Fields USA")
plt.show()

##Selecting second column series

series_two = pd.series('U.S. Field Prod')


