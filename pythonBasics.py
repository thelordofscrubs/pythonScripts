numberVariable = 5
someOtherVar =  "a string of letters or digits like 5"
someArray = [1,2,6,8]
mixedArray = [2,"string", [8,3]]
def doubler(x):
    doubledNumber = x * 2
    return doubledNumber


print("printing a string literal")

print(someOtherVar)

intVariable = 10
stringIntVar = "10"

mathOutput = intVariable + 4

mathStrOut = stringIntVar + "4"

print(mathOutput)
print(mathStrOut)

#userInput = input()

#print("you typed in ", userInput)

print("Please type in a number to double")

ugn = int(input())

dn = doubler(ugn)

print("Your number doubled is ", str(dn))

