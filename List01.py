from numpy import dot, arccos, clip
from numpy.linalg import norm
from list01_functions import Functions
from random import randint

class List01():
    def __init__(self):
        List01.task1(self)
        List01.task2(self)
        List01.task3(self)
        List01.task4(self)
        List01.task5(self)
        List01.task6(self)
        List01.task7(self, "hello pyt8989hon")
        # List01.task8(self)
        List01.task9(self, "abracadabra")
        List01.task10(self, 7)

    def task1(self,):
        print("-------- task 1 ----------")
        number = eval(input("Put int number: "))
        if type(number) == int:
            Functions.odd_even_check(number)
        else:
            return print("This number is not a int!")


    def task2(self):
        print("-------- task 2 ----------")
        list = Functions.random_function(20)
        print("min value of", list, "is: ", min(list))
        print("max value of ", list, "is: ", max(list))
        return 0

    def task3(self):
        print("-------- task 3 ----------")
        vector1 = [1,2,3,4,5]
        vector2 = [6,7,8,9,8]
        result = dot(vector1, vector2)/norm(vector1)/norm(vector2)
        angle = arccos(clip(result, -1, 1))
        return print("angle: ", angle)

    def task4(self):
        print("-------- task 4 ----------")
        list = Functions.random_function(30)
        c = randint(1, 5)
        a = list[0]
        b = list[-1]
        print("c: ", c, "a: ", a, "b:", b)
        greaterThanA = []
        smallerThanb = []

        for item in list:
            if (item > a and item % c == 0):
                greaterThanA.append(item)
            elif (item < b and item % c == 0):
                smallerThanb.append(item)
        print("full list: ", list)
        print("smaller than b: ", smallerThanb)
        print("bigger than a: ", greaterThanA)

    def task5(self):
        print("-------- task 5 ----------")
        listA = Functions.random_function(10)
        listB = Functions.random_function(12)
        common_items = set(listA) - (set(listA) - set(listB))
        print("List 1: ", listA)
        print("List 2: ", listB)
        print("Common: ", common_items)

    def task6(self):
        print("-------- task 6 ----------")
        x = "abracadabra"
        stringList = []

        #for letter in str(x):
        #  stringList1.append(letter)
        #  stringList1.remove('a')

        for letter in str(x):
            if letter != "a":
                stringList.append(letter)
            else:
                pass
        print(stringList)


    def task7(self, sentence):
        print("-------- task 7 ----------")
        sentence = str(sentence)
        digit = 0
        letter = 0
        return Functions.is_digit(sentence, digit, letter)

    def task8(self):
        print("-------- task 8 ----------")
        set = [1, 2, 3, 4]
        subset = []
        return print(sorted(sum(set, subset)), "\n", type(set), type(subset))


    def task9(self, sentence):
        print("-------- task 9 ----------")
        list9 = []
        for item in str(sentence):
            if item.isdigit() == False:
                list9.append(item)
            else:
                pass
        y = 0
        y1 = "zero"
        for letter in list9:
            x = list9.count(letter)
            print("letter ", letter, "is: ", x)
            if x > int(y):
                y = x
                y1 = letter
            else:
                pass
        print("most frequent letter is: ", y1, ":", y)

    def task10(self, decimal_number):
        print("-------- task 10 ----------")
        return print("Decimal number of: ", decimal_number, "is: ", bin(decimal_number))


list01 = List01()
list01.__init__()
