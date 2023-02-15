import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
path = "TurkeyDevastatingEarthquakes.csv"
Earthquakes_Turkey = pd.read_csv(path,encoding='ISO-8859-1', sep=';')
print(Earthquakes_Turkey['Location'])
Earthquakes_Turkey.drop(columns="Time",axis=1,inplace=True)
Earthquakes_Turkey.drop(columns="Location",axis=1,inplace=True)
Earthquakes_Turkey.drop(columns="Long.",axis=1,inplace=True)
Earthquakes_Turkey.drop(columns="Lat.",axis=1,inplace=True)
Earthquakes_Turkey.drop(columns="Focal Depth (km)",axis=1,inplace=True)
Earthquakes_Turkey.drop(columns="Fault Mechanism,,,,",axis=1,inplace=True)

Earthquakes_Turkey.replace('6.3 (Ms)',6.3,inplace=True)
Earthquakes_Turkey.replace('6.3 (Mw)',6.3,inplace=True)
Earthquakes_Turkey.replace('6.0 (Mw)',6.0,inplace=True)
Earthquakes_Turkey.replace('6,1 (Ms)',6.1,inplace=True)
Earthquakes_Turkey.replace('6.1 (Ms)',6.1,inplace=True)
Earthquakes_Turkey.replace('6,1 (Mw)',6.1,inplace=True)
Earthquakes_Turkey.replace('6,2 (Ms)',6.2,inplace=True)
Earthquakes_Turkey.replace('6.2 (Ms)',6.2,inplace=True)
Earthquakes_Turkey.replace('6,3 (Mw)',6.3,inplace=True)
Earthquakes_Turkey.replace('6.3 (Mw)',6.3,inplace=True)
Earthquakes_Turkey.replace('6.4 (Mw)',6.4,inplace=True)
Earthquakes_Turkey.replace('6.5 (Ms)',6.5,inplace=True)
Earthquakes_Turkey.replace('6.5 (Mw)',6.5,inplace=True)
Earthquakes_Turkey.replace('6.6 (Ms)',6.6,inplace=True)
Earthquakes_Turkey.replace('6.6 (Mw)',6.6,inplace=True)
Earthquakes_Turkey.replace('6.7 (Mw)',6.7,inplace=True)
Earthquakes_Turkey.replace('6.7 (Ms)',6.7,inplace=True)
Earthquakes_Turkey.replace('6.8 (Ms)',6.8,inplace=True)
Earthquakes_Turkey.replace('6.9 (Ms)',6.9,inplace=True)
Earthquakes_Turkey.replace('7.0 (Ms)',7,inplace=True)
Earthquakes_Turkey.replace('7.1 (Mw)',7.1,inplace=True)
Earthquakes_Turkey.replace('7.1 (Ms)',7.1,inplace=True)
Earthquakes_Turkey.replace('7.2 (Mw)',7.2,inplace=True)
Earthquakes_Turkey.replace('7.2 (Ms)',7.2,inplace=True)
Earthquakes_Turkey.replace('7.3 (Ms)',7.3,inplace=True)
Earthquakes_Turkey.replace('7.4 (Ms)',7.4,inplace=True)
Earthquakes_Turkey.replace('7.5 (Mw)',7.5,inplace=True)
Earthquakes_Turkey.replace('7.9 (Ms)',7.9,inplace=True)
Earthquakes_Turkey.rename(columns={'Mag.':'Magnitude'},inplace=True)
print(Earthquakes_Turkey)


plt.figure(figsize=(10,8))
plt.scatter(Earthquakes_Turkey.Date,Earthquakes_Turkey.Casualty)
plt.ylabel('Casualties')
plt.xlabel('Year')
plt.title('Casualties in Earthquakes by Year (Turkey)')
plt.show()

#graph
plt.figure(figsize=(10,8))
plt.plot(Earthquakes_Turkey.Date,Earthquakes_Turkey.Magnitude)
plt.ylabel('Magnitude')
plt.xlabel('Year')
#changing the appearance of the title
plt.title('Magnitude of Earthquakes by Year (Turkey)',\
          fontdict={'fontname':'Comic Sans MS','fontsize':18})
plt.show()

plt.figure(figsize=(10,8))
plt.bar(Earthquakes_Turkey.Date,Earthquakes_Turkey.Casualty,)
plt.ylabel('Casualties')
plt.xlabel('Year')
plt.yticks(Earthquakes_Turkey.Casualty[::2])
#changing the appearance of the title
plt.title('Casualties in Earthquakes by Year (Turkey)',\
          fontdict={'fontname':'Comic Sans MS','fontsize':18})
plt.show()
Earthquakes_Turkey.Casualty = [int(x.strip('+')) if type(x)==str else x for x in \
        Earthquakes_Turkey.Casualty]
# print(sns.distplot(Earthquakes_Turkey['Casualty'],kde=False,bins=10))
# plt.show()
sns.jointplot(x='Date',y='Casualty',data=Earthquakes_Turkey,kind='hex')
# plt.title('Earthquakes in Turkey')
plt.show()
