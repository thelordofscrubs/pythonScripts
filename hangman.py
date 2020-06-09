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

print("Type in a work for the other player to guess:")
word = input()

wordLength = len(word)

gameRunning = True
checkLetters = True

while gameRunning:
    system("cls")
    print("\n\n\n")
    printGame(wordLength)
    checkLetters = True
    for x in range(wordLength):
        if not (word[x] in correctGuesses):
            checkLetters = False
    if checkLetters == True:
        break
    print("Guess a letter from the list:")
    guess = input()
    if guess in word:
        correctGuesses.append(guess)
    pastGuesses.append(guess)

print("Congratulatiuons, you Won!")