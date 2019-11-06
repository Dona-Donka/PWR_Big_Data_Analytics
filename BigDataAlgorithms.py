from collections import Counter

dictFile = open("file.txt", "w")
with open ("book.txt") as mybook:
    list = Counter(mybook.read().split())

list = dict(list)

for key, value in sorted(list.items(), key=lambda item: item[1], reverse=True):
    dictFile.write("%s %s \n" % (key, value))

##########################################################################################
# TD-IDF
sum_of_words = 0
for key, value in word_list.items():
    sum_of_words += value

print("sum: ", sum_of_words)
for key, value in sorted(word_list.items(), key=lambda item: item[1], reverse=True):
    print("word: ", key, "TD-IDF: ", value, "/", sum_of_words, "=", value/sum_of_words)

##########################################################################################
# k-shingle, Jaccard similarity

import binascii

f1 = open(PATH, "r")
f2 = open(PATH, "r")

def words_tab(f):
    tab = []
    for line in f:
        for word in line.split():
            tab.append(word)
    return tab

words_from_file1 = words_tab(f1)
words_from_file2 = words_tab(f2)

def shingle(tab):
    k = 7
    shingle_tab = []

    for i in range(0, len(tab)):
        shingle = tab[i:i+k]
        shingle = ' '.join(shingle)
        shingle_tab.append(int(''.join(format(ord(i), 'b') for i in shingle)))
    return shingle_tab

file1 = set(shingle(words_from_file1))
file2 = set(shingle(words_from_file2))

inter = file1.intersection(file2)
print("Jaccard similarity: ", float(len(inter)) / (len(file1) + len(file2) - len(inter)))
