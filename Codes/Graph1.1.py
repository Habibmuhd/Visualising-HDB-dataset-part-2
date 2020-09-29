import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
plt.style.use("fivethirtyeight")


df = pd.read_csv('Data/resale-transactions-by-flat-type-based-on-registered-cases.csv')

#select each room flats
one_room = df.loc[df['flat_type'] == '1 room']
two_room = df.loc[df['flat_type'] == '2 room']
three_room = df.loc[df['flat_type'] == '3 room']
four_room = df.loc[df['flat_type'] == '4 room']
five_room = df.loc[df['flat_type'] == '5 room']


fig, ax = plt.subplots(1, figsize=(10,10))  #Creates just a figure and only one subplot

#ax.plot(one_room['financial_year'], one_room['resale_transactions'], label= "1-room", linestyle= "-" )
#ax.plot(one_room['financial_year'], two_room['resale_transactions'], label= "2-room", linestyle= "--" )
ax.plot(one_room['financial_year'], three_room['resale_transactions'], label= "3-room", linestyle= ":" )
ax.plot(one_room['financial_year'], four_room['resale_transactions'], label= "4-room", linestyle= "--" )
ax.plot(one_room['financial_year'], five_room['resale_transactions'], label= "5-room", linestyle= "-" )
ax.set_xlabel("Financial Year") #set the x-axis name
ax.set_ylabel("Number of transactions") #set the yaxis name
plt.xticks(rotation=0)
ax.tick_params(axis='y')

ax.set_title('HDB Resale Flat transaction',fontsize=18, y=1.03)
fig.tight_layout() #otherwise the right y-label is slightly clipped
plt.legend(loc="upper right")
plt.show()
