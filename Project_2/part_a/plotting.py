import matplotlib.pyplot as plt
import json
import numpy as np

# Opening JSON file
with open('data.json') as json_file:
    data = json.load(json_file)
print(type(data))
size = list(data.keys())
runtime = list(data.values())
size = [int(i) for i in size]
print(size)
print(runtime)


def f(x):
    return 4/10000000 * x * x


x = np.linspace(100, 9900, 1000)

#fig, axs = plt.subplots(1, 4)
plt.plot(x, f(x), color='red', label='f(x) = x^2', linestyle='dashed')
plt.plot(size, runtime, label='Dijkstra (array,adj matrix)')

plt.xlabel('Graph Size')
plt.ylabel('Runtime(s)')
plt.legend()
plt.show()
