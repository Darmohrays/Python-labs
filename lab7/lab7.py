import pandas as pd
import matplotlib.pyplot as plt
import numpy

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (10, 5)

df = pd.read_csv('NYC_Jobs.csv')

#print(df[['Agency']] [:10])

#print(df[['Agency', 'Business Title', 'Work Location']])

agency_counts = df['Agency'].value_counts()

#print(agency_counts)

agency_counts[:10].plot(kind='bar')
plt.show()

range_to = df['Salary Range To']
range_from = df['Salary Range From']

s = (range_from + range_from)/2

df['s'] = s

print(df['s'])

df.set_index('Work Location')['s'].plot(kind='bar')

plt.show()