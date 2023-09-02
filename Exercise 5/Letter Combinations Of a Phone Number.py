from collections import defaultdict
digits = int(input())
d = defaultdict(list)
d = {
     "2":["a","b","c"],
     "3":["d","e","f"],
     "4":["g","h","i"],
     "5":["j","k","l"],
     "6":["m","n","o"],
     "7":["p","q","r","s"],
     "8":["t","u","v"],
     "9":["w","x","y","z"]}
n = len(digits)
result = []
for i in range(n):
    temp = []
    if result == []:
        result = d[digits[i]]
        continue
    for val in result:
        for c in d[digits[i]]:
            temp.append(str(val + c))
    result = temp
print(result)