import pandas as pd
import matplotlib.pyplot as plt
import pygal
import lxml
import numpy as np
import mysql.connector
import seaborn as sns
from pygal.style import CleanStyle

mydb = mysql.connector.connect(host= 'localhost',user = 'Habib',passwd= '123',database='ca2')  #open connection

cur = mydb.cursor() #sets a pointer in sql table

df = pd.read_sql('SELECT * FROM transaction',con=mydb)
mydb.close()
#print (df)


bool_series = pd.isnull(df['represented'])
#print(df[bool_series]) #no data with empty text

bool_series = pd.isnull(df['town_txt'])
#print(df[bool_series])  #no data with empty text

df1 = df.drop(columns=['complete_date_txt','salesperson_name','salesperson_reg_no'])
#print(df1)

"""print(df1.head())
print(df1.shape)
print(df1.dtypes)"""


buyer_data = df1[df1['represented'] == 'Buyer']
seller_data = df1[df1['represented'] == 'Seller']





#buyer data only

tot_buyer = buyer_data.shape[0]

bpp_buyer = buyer_data[buyer_data['town_txt'] == 'BUKIT PANJANG']
num_bpp_buyer = bpp_buyer.shape[0]

tamp_buyer = buyer_data[buyer_data['town_txt'] == 'TAMPINES']
num_tamp_buyer = tamp_buyer.shape[0]

wood_buyer = buyer_data[buyer_data['town_txt'] == 'WOODLANDS']
num_wood_buyer = wood_buyer.shape[0]

pun_buyer = buyer_data[buyer_data['town_txt'] == 'PUNGGOL']
num_pun_buyer = pun_buyer.shape[0]

hou_buyer = buyer_data[buyer_data['town_txt'] == 'HOUGANG']
num_hou_buyer = hou_buyer.shape[0]

ang_buyer = buyer_data[buyer_data['town_txt'] == 'ANG MO KIO']
num_ang_buyer = ang_buyer.shape[0]

rem_buyers = tot_buyer - (num_ang_buyer + num_bpp_buyer + num_hou_buyer + num_pun_buyer + num_tamp_buyer + num_wood_buyer)

print(tot_buyer,rem_buyers)


#seller data only

tot_seller = seller_data.shape[0]


bpp_seller = seller_data[seller_data['town_txt'] == 'BUKIT PANJANG']
num_bpp_seller = bpp_seller.shape[0]

tamp_seller = seller_data[seller_data['town_txt'] == 'TAMPINES']
num_tamp_seller = tamp_seller.shape[0]

wood_seller = seller_data[seller_data['town_txt'] == 'WOODLANDS']
num_wood_seller = wood_seller.shape[0]

pun_seller = seller_data[seller_data['town_txt'] == 'PUNGGOL']
num_pun_seller = pun_seller.shape[0]

hou_seller = seller_data[seller_data['town_txt'] == 'HOUGANG']
num_hou_seller = hou_seller.shape[0]

ang_seller = seller_data[seller_data['town_txt'] == 'ANG MO KIO']
num_ang_seller = ang_seller.shape[0]

rem_sellers = tot_seller - (num_ang_seller + num_bpp_seller + num_hou_seller + num_pun_seller + num_tamp_seller + num_wood_seller)

print(tot_seller,rem_sellers)


pie_chart= pygal.Pie()
pie_chart.title = 'Breakdown (in %) of buyers in towns for 3 years (2017-2020)'
pie_chart.add('Ang Mo Kio', num_ang_buyer)
pie_chart.add('Bukit Panjang', num_bpp_buyer)
pie_chart.add('Hougang', num_hou_buyer)
pie_chart.add('Tampines', num_tamp_buyer)
pie_chart.add('Punggol', num_pun_buyer)
pie_chart.add('Woodlands', num_wood_buyer)
pie_chart.add('Other towns', rem_buyers)
pie_chart.render_in_browser()