import random
import matplotlib.pyplot as plt
import numpy as np
import itertools

def value_list(number_of_drunk_sailors, xn):

    sailorList = []
    stepsList = []
    xnList = []
    xNaList = []
    for item in range(1, xn):
        xnList.append(item)

    N = np.arange(number_of_drunk_sailors)

    for sailor in range(0, number_of_drunk_sailors):
        xNa = 0
        x = 0
        for item in range(1, xn):
            R =random.uniform(0,1)

            if R < 0.5:
                x = x + 1
            else:
                x = x - 1

        xNa = xNa + x
        stepsList.append(x)
        xNaList.append(xNa)

    return (xNaList)

def various_value(xNaList):
    std = np.std(xNaList)
    return std

# dict used to create histograms of posiotions xn after N steps
# for K - number of drunkards
def createDict(list):
    list = sorted(list)
    dictListKeys = []
    dictListValues = []
    for number in list:
        value = list.count(number)
        dictListKeys.append(number)
        dictListValues.append(value)

    dictionary_xNa = dict(zip(dictListKeys, dictListValues))
    return dictionary_xNa


xNaDictionary_1 = createDict(value_list(30000, 100))
xNaDictionary_2 = createDict(value_list(30000, 1000))
xNaDictionary_3 = createDict(value_list(30000, 10000))

listOf_xn = []
stepList = []

for step in range(10,3000, 100):
    listOf_xn.append(various_value(value_list(30000, step )))
    stepList.append(step)
    print(step, "\n")

#print(listOf_xn)
#print(stepList)


# Histograms of posiotions Xn after N=100 steps
#figure1, axs = plt.subplots(3, 1)
#axs[0].bar(xNaDictionary_1.keys(), xNaDictionary_1.values(), 0.7)
#axs[1].bar(xNaDictionary_2.keys(), xNaDictionary_2.values(), 0.7)
#axs[2].bar(xNaDictionary_3.keys(), xNaDictionary_3.values(), 0.7)

#plt.ylabel('Number of drunkards')
#plt.xlabel('Number of steps')
#plt.show()

#................. Standard deviation and trendline.................#

plt.plot(np.log(stepList), np.log(listOf_xn), 'go', label='Standard deviation')
plt.ylabel('standard deviation')
plt.xlabel('Number of steps')

z = np.polyfit(np.log(stepList), np.log(listOf_xn), 1)
plt.plot(np.log(stepList), np.log(stepList)*z[0] + z[1],"r--", label = 'Trendline')
plt.legend(loc='upper left', prop={'size': 10})
print("regresja: ", z)
plt.show()

