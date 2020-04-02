import random
import pdfkit
random.seed()
f = open("cnwords.txt")
wordsArray = []
word = "Non"
while True:
    word = f.readline()
    if (word == ""):
        break
    word = word[:-1]
    wordsArray.append(word)

f.close()
length = len(wordsArray)
#
#for o in range(0,5):
#    f = open("codenamesBoard" + str(o+1) + ".txt","w")
#    wordList = []
#    x = 0
#    while x < 25:
#        word = wordsArray[random.randrange(length)]
#        if not (word in wordList):
#            wordList.append(word)
#            x+=1
#    for x in range(0,5):
#        f.write("{:_^15}|{:_^15}|{:_^15}|{:_^15}|{:_^15}\n".format(*wordList[x*5:x*5+5]))
#    f.close()
#