import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
plt.style.use("ggplot")

df = pd.read_csv('Data/housing-and-development-board-resale-price-index-1q2009-100-quarterly.csv')

print(df.head())
print(df.shape)
print(df.dtypes)


fig, ax = plt.subplots(1, figsize=(10,10))  #Creates just a figure and only one subplot
ax.plot(df['quarter'], df['index'], label= "Resale Price Index", linestyle= "-" )
ax.set_xlabel("Quarter") #set the x-axis name
ax.set_ylabel("Index") #set the yaxis name
plt.xticks(rotation=90)
ax.tick_params(axis='y')



ax.xaxis.set_major_locator(plt.MultipleLocator(4))

ax.set_title('HDB Resale Flat Index over the years',fontsize=18, y=1.03)
fig.tight_layout() #otherwise the right y-label is slightly clipped
plt.legend(loc="upper left")
plt.show()