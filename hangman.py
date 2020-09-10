from os import system
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
pastGuesses = []
correctGuesses = []
def printGame(wl):
    wordDisplay = "      "
    for x in range(wl):
        if word[x] in correctGuesses:
            wordDisplay += " "+word[x]+" "
        else:
            wordDisplay = wordDisplay + " _ "
    print(wordDisplay)
    print("\n\n")
    alphToDisp = ""
    for x in range(2):
        for y in range(13):
            if alphabet[x*13+y] in pastGuesses:
                alphToDisp += "_, "
            else:
                alphToDisp += alphabet[x*13+y] + ", "
        print(alphToDisp)
        alphToDisp = ""

def isGameLost(x, y):
    isXGreater = False
    if x >= y:
        isXGreater = True
    return isXGreater

print("Type in a word for the other player to guess:")
word = input()
wordLength = len(word)
gameRunning = True
checkLetters = True
numberOfGuesses = 0
maxNumberOfGuesses = 6
while gameRunning:
    guess = ""
    system("cls")
    print("\n\n\n")
    printGame(wordLength)
    print("\nYou have {0} tries left\n".format(maxNumberOfGuesses-numberOfGuesses))
    checkLetters = True
    for x in range(wordLength):
        if not (word[x] in correctGuesses):
            checkLetters = False
    if checkLetters == True:
        print("Congratulatiuons, you Won!")
        break
    if isGameLost(numberOfGuesses, maxNumberOfGuesses) == True:
        print("You have run out of tries")
        break
    print("Guess a letter from the list:")
    while not (guess in alphabet):
        guess = input()
        if not (guess in alphabet):
            print("\nThat is not a valid guess, please try again\n")
    if guess in word:
        correctGuesses.append(guess)
    else:
        numberOfGuesses += 1 #numberOfGuesses = numberOfGuesses + 1
    pastGuesses.append(guess)
    
