import pandas as pd
import matplotlib.pyplot as plt
import numpy

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (10, 5)

df = pd.read_csv('NYC_Jobs.csv')

print(df[['Agency']] [:10])

print(df[['Agency', 'Business Title', 'Work Location 1']] [0:])

agency_counts = df['Agency'].value_counts()

print(agency_counts)

agency_counts[:10].plot(kind='bar')
plt.show()

gp3 = df.groupby(['Work Location'])['Salary Range From', 'Salary Range To'].mean()

errors = gp3.std()

print(gp3)

fig, ax = plt.subplots()

gp3.plot.bar(yerr=errors, ax=ax)
plt.show()