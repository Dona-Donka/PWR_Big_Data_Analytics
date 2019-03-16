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
    nltk.download('gutenberg')

    return 0


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
print(task07())
