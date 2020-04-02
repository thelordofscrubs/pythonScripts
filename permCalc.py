def findPerm(n, r):
    result = 1
    for x in range(n, n-r, -1):
        result *= x
    return result


minimumPerms = findPerm(400,25)
print(minimumPerms)
i = 1
while True:
    currentPerms = findPerm(50000, i)
    if currentPerms >= minimumPerms:
        break
    i += 1

print(i)