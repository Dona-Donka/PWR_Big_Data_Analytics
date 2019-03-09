import random
import itertools

class Functions():
    def random_function(len):
        list = []
        x = 0
        while x < len:
            list.append(random.randint(1, 90))
            x += 1
        return list


    def odd_even_check(x):
        if (x % 2 == 0):
            return print(x, "is a odd number")
        else:
            return print(x, "is an even number")


    def is_digit(sentence, digit, letter):

        if sentence.isdigit() == True:
            print("This is not a sentence! This is a digit")
        elif sentence.isalpha() == True:
            print("This is not a sentence! This is an alpha")
        else:
            for item in sentence:
                if item.isdigit() == True:
                    digit += 1
                elif item.isalpha() == True:
                    letter += 1
        return print("sentence: ", sentence, "\n", "number of letter: ", letter, "\n", "number of digit: ", digit, "\n" )
    
    def subset(numbersSet, item):
        return set(itertools.combinations(numbersSet, item))
