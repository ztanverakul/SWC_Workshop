import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('/mnt/c/users/john/documents/github/data/gapminder_gdp_europe.csv', index_col='country')
#print(data.describe())

#data.to_csv('fun.csv')

#print(data.iloc[2, 1])

#print(data.loc["Belgium", "gdpPercap_1957"])

#print(data.loc["Albania", :])

#print(data.loc[:, "gdpPercap_1952"])

subset = data.loc['Italy':'Poland', 'gdpPercap_1962':'gdpPercap_1972']

mask = subset > 10000
print(subset[mask])

mask_higher = data.apply(lambda x:x>x.mean())
print(mask_higher)

'''
time =[0, 1, 2, 3]
position = [0, 100, 200, 300]

plt.plot(time, position).show(
plt.xlabel('Time (hr)')
plt.ylabel('Position (km)')
'''
