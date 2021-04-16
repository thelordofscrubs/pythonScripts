inp = input("please input value to be hashed\n")

try:
    inp = int(inp)

except:
    inp = inp.encode('utf-8','namereplace')

output = ""

try:
    output = bin(inp)

except:
    for bit in inp:
        output = output+str(bin(bit))

try:
    print(bin(output))
except:
    print("bare: "+output)

def blen(i):
    return len(bin(i[2:]))

def getHash(inputBin):
    inputlen = blen(inputBin)
    currentVal = (inputBin << 1) | 1
    currentVal = currentVal << (512%inputlen)
    currentVal += inputlen
