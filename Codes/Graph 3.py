import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression



plt.style.use("seaborn")

df = pd.read_csv('Data/land-area-and-dwelling-units-by-town.csv')

latest_data = df.loc[df['financial_year'] == 2018]
latest_data2 = latest_data[latest_data.dwelling_units_under_management != '-']
latest_data1 = latest_data2.sort_values(['dwelling_units_under_management'],ascending= True)
latest_data1['dwelling_units_under_management'] = latest_data1['dwelling_units_under_management'].astype(str).astype(float)
print(latest_data1.dtypes)


print(df.head())
print(df.shape)
print(df.dtypes)

labels = latest_data1['town']

print(latest_data1)


#for regression line
X = latest_data1.iloc[:,3].values.reshape(-1,1)
Y= latest_data1.iloc[:,4].values.reshape(-1,1)
linear_regressor = LinearRegression()  # create object for the class
linear_regressor.fit(X,Y)
Y_pred = linear_regressor.predict(X)


#calculate mean for x axis
x1 = latest_data1.loc[:, 'residential_land_area'].mean()
y1 = latest_data1.loc[:, 'dwelling_units_under_management'].mean()
print (y1)



#print (Y_pred)

fig, ax = plt.subplots()
ax.scatter(latest_data1['residential_land_area'],latest_data1['dwelling_units_under_management'])
ax.plot(X,Y_pred,color= 'red')
plt.axhline(y=y1, color='green', linestyle='-')
plt.axvline(x=x1, color='green', linestyle='-')
plt.title("Number of units vs Residential Land area in 2018 (Density)", fontsize=18, y=1.03)
plt.xlabel('Residential land area (hectares)')
plt.ylabel('Dwelling units')




h = latest_data1["residential_land_area"]  #residential_land_area"
y = latest_data1["dwelling_units_under_management"]

for i, txt in enumerate(labels):   #label each plot
    plt.annotate(txt, (h.iloc[i], y.iloc[i]), horizontalalignment='right', verticalalignment='bottom', xytext=(45, -20), textcoords='offset pixels',)


ax.legend()
plt.show()