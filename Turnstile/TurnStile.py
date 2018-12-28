import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

turnsData = pd.read_csv("turnstiles.csv")
turnsLtrain = turnsData[ turnsData["STATION"] == "14 ST-UNION SQ" ]
myTurns = turnsLtrain[ turnsLtrain["SCP"] == "02-00-01"]

myTurns["Entries - Exits"] = myTurns["ENTRIES"] - myTurns["EXITS"]

sns.set(style="darkgrid")
fig1 = plt.figure()
sns.lineplot(x = 'DATE', y='EXITS', data=myTurns);

fig2= plt.figure()
sns.lineplot(x='DATE', y='ENTRIES', data=myTurns);

fig3 = plt.figure()
sns.lineplot(x='DATE', y='Entries - Exits', data=myTurns);


fig1.savefig('fig1.png')
fig2.savefig('fig2.png')
fig3.savefig('fig3.png')
