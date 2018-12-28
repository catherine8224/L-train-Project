import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

turnsData = pd.read_csv("turnstiles.csv")
turnsLtrain = turnsData[ turnsData["STATION"] == "14 ST-UNION SQ"]
turnsLtrain4 = turnsLtrain[ turnsLtrain["TIME"] == "4:00:00"]
turnsLtrain8 = turnsLtrain[ turnsLtrain["TIME"] == "8:00:00"]
entries = turnsLtrain8.groupby(by=['DATE'])['ENTRIES'].sum() - turnsLtrain4.groupby(by=['DATE'])['ENTRIES'].sum()
en = entries.to_frame().reset_index()

exits = turnsLtrain8.groupby(by=['DATE'])['EXITS'].sum() - turnsLtrain4.groupby(by=['DATE'])['EXITS'].sum()
ex = exits.to_frame().reset_index()

sns.set(style = "darkgrid")
fig1 = plt.figure()
sns.barplot(x="DATE", y="ENTRIES", data=en, palette = "Set3")
fig1.savefig("snap1.png")
plt.show()

fig2 = plt.figure()
sns.barplot(x="DATE", y="EXITS", data=ex)
fig2.savefig("snap2.png")
plt.show()
