import pandas as pd
d = pd.read_excel(r'/Users/josh/Desktop/Book2.xlsx', "Sheet3")
d = d.drop(['Unnamed: 6', 'Unnamed: 7', 'PH', 'NAOH%', 'E/A RATIO', 'SAMPLE SOURCE (pH info, %Extractant, E/A ratios)', 'SET data set'], axis = 1)
d = d.drop("Comment", axis = 1)
#d = d.dropna(axis = 0, how= 'all')
pd.set_option("display.max_rows", None, "display.max_columns", None)
ppm = d.groupby(['SAMPLE ID', 'DATE', 'SAMPLE REF'])[['DATE','SAMPLE ID', 'Li-(ppm)', 'Mg (ppm)']].sum().reset_index()

import matplotlib.pyplot as plt

Settlers = []
Date = []
counter = 0
for i in ppm['SAMPLE ID']:
    if i == 'BS1':
        Date.append(ppm['DATE'][counter])
        Settlers.append(ppm['Li-(ppm)'][counter])
    counter +=1
fig = plt.figure(figsize=(10,5))
plt.bar(Date, Settlers, 1,  alpha = .5)

plt.xticks(Date)
plt.show()


