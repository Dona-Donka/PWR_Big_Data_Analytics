from random import randint
import operator
from nltk.book import *
from nltk.tokenize import sent_tokenize, word_tokenize

def task01(min, max):
    listOfInt = [randint(min, max) for n in range(1, 20)]
    listOfInt = [x for x in listOfInt if x >= 0]
    return listOfInt

def task02(list):
    list = [x for x in list if len(x) < 6]
    return (list)

def task03(list):
    maxString = ""
    for name in list:
        if len(name) > len(maxString):
            maxString = name
    return maxString

def task04(listA, listB):
    listA = [x for x in listA if len(x) == len(listA[0])]
    index = 2
    for i in range(1,len(listB)):
        if len(listB[i]) ==len(listA[0]):
            listA.insert(-1 + index, listB[i])
            index +=2

    return listA

def taskk05(list):
    listOfStrings = [x for x in list if type(x) == 'str']
    listOfInt = [x for x in list if type(x) == 'int']
    sorted(listOfStrings)
    sorted(listOfInt)

def task05(list):
    strList = sorted([x for x in list if not isinstance(x, int)])
    intList = sorted([x for x in list if not isinstance(x, str)])
    return strList + intList

def task06(usersDataDict):
    return sorted(usersDataDict.items(), key=operator.itemgetter(1))

def task07():
    a = text6.count("knight")
    b = text7.count("knight")
    return (" 'knight' in text6: ", a,  "\n",
            " 'knight' in text7: ", b,)

def task8():
    listOftext6 = [x for x in text6]
    listOftext7 = [x for x in text7]
    c = [x for x in  listOftext6 if x not in listOftext7]
    return c

def task9():
    t1 = set(text1)
    t2 = set(text2)
    t3 = set(text3)
    t4 = set(text4)
    t5 = set(text5)
    t6 = set(text6)
    t7 = set(text7)
    t8 = set(text8)
    t9 = set(text9)
    allSets = t1 & t2 & t3 & t4 & t5 & t6 & t7 & t8 & t9
    return allSets

# - do poprawy -
def task10():
    t = list(text2)
    print(t)
    helpList = []
    counter = 0
    largestNumber = 0
    theLargestSentence = []
    for word in t:
        if word != '.':
            helpList.append(word)
            counter += 1
        else:
            if counter > largestNumber:
                largestNumber = counter
                theLargestSentence = helpList
                helpList = []
                counter = 0


    return "contain: ", largestNumber, "words",


################################
s = set([1, 2, 3 ,4, 5, 6])
a = set([2,4,7])

# union = {1, 2, 3, 4, 5, 6, 7}
print( a | s)

# intersection = {2, 4}
print( a & s)

# difference = {7}
print( a - s)
################################


#print(task01(-5,10))
listOfStrings = ["Jan", "Aaron", "Miron", "Leon", "Eliasz", "Voytech", "Stefan"]
#print(task02(listOfStrings))
#print(task03(listOfStrings))
listA = ["Yani", "Joel", "Liam","Nate", "Zbigniew"]
listB = ["Lora","Sara", "Inga", "Anna", "Wanda"]
#print(task04(listA, listB))
mixedList = [15, "Ali", -3, "Mathew", 44, 54, "Walerian"]
#print(task05(mixedList))
usersDataDict= {"Marek":"Radom", "Phillip":"Cork", "Ludwik":"Aspen", "Lea":"Berlin"}
#print(task06(usersDataDict))
#print(task07())
#print(task8())
#print(task9())
print(task10())
