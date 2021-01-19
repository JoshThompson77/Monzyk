import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel(r'/Users/josh/Desktop/Monzyk Innovations/Titration/Seasoned/Seasoned.xlsx')
df['NaOH added (L)'] = df['NaOH added (L)']*10**6
df = df.rename(columns={'NaOH added (L)': "NaOH added L 10^-6"})
df['total added'] = 0

totalAddd = df['NaOH added L 10^-6'].tolist()

counter = 0

for i in totalAddd:
    if counter == 0:
        counter = counter + 1
    else:
        totalAddd[counter] = totalAddd[counter] + totalAddd[(counter -1)]
        counter = counter + 1


df['total added'] = totalAddd
df2 = df[0:77]
df3=df2[0:56]
df.plot.scatter(x="total added", y = 'pH', title='Titration of new Piranha').set_xlabel('Microliters of NaOH')

# df2.plot.scatter(x = 'total added', y = 'pH', title='Titration of New Piranha').set_xlabel('Microliters of NaOH')

# df3.plot.scatter(x = 'total added', y = 'pH', title='Titration of New Piranha').set_xlabel('Microliters of NaOH')
plt.show()