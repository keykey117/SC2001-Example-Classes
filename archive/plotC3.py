import matplotlib.pyplot as plt
import json
  
# Opening JSON file
f = open('c3_3.txt')
result3 = json.load(f)
S_values3=list(result3.keys())
keyComparisons3=list(result3.values())

minComp3= min(keyComparisons3)
best3S=S_values3[keyComparisons3.index(minComp3)]
print(f'best S value for 10^3 is {best3S}')

f = open('c3_4.txt')
result4 = json.load(f)
S_values4=list(result4.keys())
keyComparisons4=list(result4.values())

minComp4= min(keyComparisons4)
best4S=S_values4[keyComparisons4.index(minComp4)]
print(f'best S value for 10^4 is {best4S}')


f = open('c3_5.txt')
result5 = json.load(f)
S_values5=list(result5.keys())
keyComparisons5=list(result5.values())
minComp5= min(keyComparisons5)
best5S=S_values5[keyComparisons5.index(minComp5)]
print(f'best S value for 10^5 is {best5S}')

f = open('c3_6.txt')
result6 = json.load(f)
S_values6=list(result6.keys())
keyComparisons6=list(result6.values())
minComp6= min(keyComparisons6)
best6S=S_values6[keyComparisons6.index(minComp6)]
print(f'best S value for 10^6 is {best6S}')
#graph plotting X is S, Y is key comparisons


#fig, axs = plt.subplots(1, 4)
fig, axs = plt.subplots(4)
axs[0].plot(S_values3, keyComparisons3, label='Array length 10^3')
axs[1].plot(S_values4, keyComparisons4, 'tab:orange', label='Array length 10^4')
axs[2].plot(S_values5, keyComparisons5, 'tab:green', label='Array length 10^5')
axs[3].plot(S_values6, keyComparisons6, 'tab:red', label='Array length 10^6')
for ax in axs.flat:
    ax.set(xlabel='S Value', ylabel='Key Comparisons')
plt.legend()
plt.show()