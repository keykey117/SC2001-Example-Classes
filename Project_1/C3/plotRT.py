import matplotlib.pyplot as plt

result3={}
with open('HybridSortCPP/ConsoleApplication1/resultsRunTime3.txt') as data:
    datalines = (line.rstrip('\r\n') for line in data)
    for idx, value in enumerate(datalines):
        result3[idx+1]=value
S_values3=list(result3.keys())
rt3=list(result3.values())
rt3 = [int(line) for line in rt3]

result4={}
with open('HybridSortCPP/ConsoleApplication1/resultsRunTime4.txt') as data:
    datalines = (line.rstrip('\r\n') for line in data)
    for idx, value in enumerate(datalines):
        result4[idx+1]=value        
S_values4=list(result4.keys())
rt4=list(result4.values())
rt4 = [int(line) for line in rt4]

result5={}
with open('HybridSortCPP/ConsoleApplication1/resultsRunTime5.txt') as data:
    datalines = (line.rstrip('\r\n') for line in data)
    for idx, value in enumerate(datalines):
        result5[idx+1]=value      
S_values5=list(result5.keys())
rt5=list(result5.values())
rt5 = [int(line) for line in rt5]

result6={}
with open('HybridSortCPP/ConsoleApplication1/resultsRunTime6.txt') as data:
    datalines = (line.rstrip('\r\n') for line in data)
    for idx, value in enumerate(datalines):
        result6[idx+1]=value  
S_values6=list(result6.keys())
rt6=list(result6.values())
rt6 = [int(line) for line in rt6]

result7={}
with open('HybridSortCPP/ConsoleApplication1/resultsRunTime7.txt') as data:
    datalines = (line.rstrip('\r\n') for line in data)
    for idx, value in enumerate(datalines):
        result7[idx+1]=value  
S_values7=list(result7.keys())
rt7=list(result7.values())
rt7 = [int(line) for line in rt7]


fig, axs = plt.subplots(5)
axs[0].plot(S_values3, rt3, label='Array length 10^3')
axs[1].plot(S_values4, rt4, 'tab:orange', label='Array length 10^4')
axs[2].plot(S_values5, rt5, 'tab:green', label='Array length 10^5')
axs[3].plot(S_values6, rt6, 'tab:red', label='Array length 10^6')
axs[4].plot(S_values7, rt7, 'tab:blue', label='Array length 10^7')
for ax in axs.flat:
    ax.set(xlabel='S Value', ylabel='Runtime')
plt.legend()
plt.show()