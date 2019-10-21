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
