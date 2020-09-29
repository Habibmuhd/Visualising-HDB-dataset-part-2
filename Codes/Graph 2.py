import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pygal
import lxml
from pygal.style import CleanStyle

plt.style.use("ggplot")

df = pd.read_csv('Data/resale-flat-prices-based-on-registration-date-from-jan-2017-onwards.csv')


"""print(df.head())
print(df.shape)
print(df.dtypes)"""

#select areas
bpp = df.loc[(df['flat_type'] == '4 ROOM') & (df['town'] == 'BUKIT PANJANG')]
tamp = df.loc[(df['flat_type'] == '4 ROOM') & (df['town'] == 'TAMPINES')]
woodlands = df.loc[(df['flat_type'] == '4 ROOM') & (df['town'] == 'WOODLANDS')]
punggol = df.loc[(df['flat_type'] == '4 ROOM') & (df['town'] == 'PUNGGOL')]
amk = df.loc[(df['flat_type'] == '4 ROOM') & (df['town'] == 'ANG MO KIO')]
hougang = df.loc[(df['flat_type'] == '4 ROOM') & (df['town'] == 'HOUGANG')]

box_plot = pygal.Box(box_mode="1.5IQR", human_readable=True, style=CleanStyle)
box_plot.title = 'Flat Prices in Various Towns'
box_plot.add('Ang Mo Kio', amk['resale_price'])
box_plot.add('Bukit Panjang', bpp['resale_price'])
box_plot.add('Hougang', hougang['resale_price'])
box_plot.add('Punggol', punggol['resale_price'])
box_plot.add('Tampines', tamp['resale_price'])
box_plot.add('Woodlands', woodlands['resale_price'])
box_plot.render_in_browser()

