import matplotlib.pyplot as plt

result3={}
with open('HybridSortCPP/ConsoleApplication1/resultsKeyComp3.txt') as data:
    datalines = (line.rstrip('\r\n') for line in data)
    for idx, value in enumerate(datalines):
        result3[idx+1]=value
S_values3=list(result3.keys())
kc3=list(result3.values())
kc3 = [int(line) for line in kc3]

result4={}
with open('HybridSortCPP/ConsoleApplication1/resultsKeyComp4.txt') as data:
    datalines = (line.rstrip('\r\n') for line in data)
    for idx, value in enumerate(datalines):
        result4[idx+1]=value        
S_values4=list(result4.keys())
kc4=list(result4.values())
kc4 = [int(line) for line in kc4]

result5={}
with open('HybridSortCPP/ConsoleApplication1/resultsKeyComp5.txt') as data:
    datalines = (line.rstrip('\r\n') for line in data)
    for idx, value in enumerate(datalines):
        result5[idx+1]=value      
S_values5=list(result5.keys())
kc5=list(result5.values())
kc5 = [int(line) for line in kc5]

result6={}
with open('HybridSortCPP/ConsoleApplication1/resultsKeyComp6.txt') as data:
    datalines = (line.rstrip('\r\n') for line in data)
    for idx, value in enumerate(datalines):
        result6[idx+1]=value  
S_values6=list(result6.keys())
kc6=list(result6.values())
kc6 = [int(line) for line in kc6]

result7={}
with open('HybridSortCPP/ConsoleApplication1/resultsKeyComp7.txt') as data:
    datalines = (line.rstrip('\r\n') for line in data)
    for idx, value in enumerate(datalines):
        result7[idx+1]=value  
S_values7=list(result7.keys())
kc7=list(result7.values())
kc7 = [int(line) for line in kc7]

fig, axs = plt.subplots(5)
axs[0].plot(S_values3, kc3, label='Array length 10^3')
axs[1].plot(S_values4, kc4, 'tab:orange', label='Array length 10^4')
axs[2].plot(S_values5, kc5, 'tab:green', label='Array length 10^5')
axs[3].plot(S_values6, kc6, 'tab:red', label='Array length 10^6')
axs[4].plot(S_values7, kc7, 'tab:blue', label='Array length 10^6')
for ax in axs.flat:
    ax.set(xlabel='S Value', ylabel='KeyComparison')
plt.legend()
plt.show()