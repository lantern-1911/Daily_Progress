string1 = input()
charset = set()
temp = 0
result = 0
for r in range(len(string1)):
    while string1[r] in charset:
        charset.remove(string1[temp])
        temp += 1
    charset.add(string1[r])
    result = max(result, r - temp + 1)
print(result)