wordArray = []
tf = open("100kWords.txt")
line = 1
while True:
    line+=1
    try:
         word = tf.readline()
    except:
        print("exception at line "+str(line))
        #break
        continue
    if not word:
        break
    if word.startswith("#"):
        continue
    if "\'" in word:
        continue
    if "." in word:
        continue
    if len(word) <= 4:
        continue
    if word[0].isupper():
        continue
    c = False
    for letter in word:
        if ord(letter) < 97 or ord(letter) > 122:
            c = True
    if c :
        continue
    wordArray.append(word)#97,122

tf.close()
tf = open("seedWords.txt", "w")
for word in wordArray:
    tf.write(word)
tf.close()
print("amount of words = "+str(len(wordArray)))