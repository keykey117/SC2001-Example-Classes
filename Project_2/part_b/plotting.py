import matplotlib.pyplot as plt
import json
  
# Opening JSON file
with open('data.json') as json_file:
    data = json.load(json_file)
print(type(data))
size=list(data.keys())
runtime=list(data.values())

#fig, axs = plt.subplots(1, 4)
fig, axs = plt.subplots(1)
axs.plot(size, runtime, label='Dijkstra min heap')
axs.set(xlabel='Graph Size', ylabel='Runtime(s)')
plt.legend()
plt.show()