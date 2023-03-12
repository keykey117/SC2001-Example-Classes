import matplotlib.pyplot as plt
import json
import math 
import numpy as np
# Opening JSON file
with open('dataNew10k.json') as json_file:
    dataAvg = json.load(json_file)
size=list(dataAvg.keys())
runtimeAvg=list(dataAvg.values())
runtimeAvg = [int(i) for i in runtimeAvg]
size = [int(i) for i in size]
with open('dataNewWorst6k.json') as json_file:
    dataWorst = json.load(json_file)
runtimeWorst=list(dataWorst.values())
y1=[]
for i in size:
    y1.append(int(i)*int(i)*math.log(int(i))*0.00000002)

y2=[]
for i in size:
    y2.append(int(i)*math.log(int(i))*0.000000055)
#fig, axs = plt.subplots(1, 4)
fig, axs = plt.subplots(1)
#axs.plot(size, runtimeWorst, label='Dijkstra min heap (empirical worst)')
axs.plot(size, runtimeAvg, label='Dijkstra min heap (empirical)')
axs.plot(size, y1, label='Dijkstra min heap (theoretical)')
#axs.plot(size, y2, label='Dijkstra min heap (theoretical best)')
axs.set(xlabel='Graph Size', ylabel='Runtime(s)')
plt.xticks(np.arange(0,max(size)+1,2000))
plt.legend()
plt.show()