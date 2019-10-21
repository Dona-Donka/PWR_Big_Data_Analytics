from collections import Counter

dictFile = open("file.txt", "w")
with open ("book.txt") as mybook:
    list = Counter(mybook.read().split())

list = dict(list)

for key, value in sorted(list.items(), key=lambda item: item[1], reverse=True):
    dictFile.write("%s %s \n" % (key, value))

##########################################################################################
