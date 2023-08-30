string1 = input()
charset = set()
for i in string1:
    if i not in charset:
        charset.add(i)
    else:
        charset.remove(i)
print(len(string1) - len(charset) + 1) if len(charset) != 0 else print(len(string1))    