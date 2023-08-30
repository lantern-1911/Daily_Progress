string1 = input()
result = ""
for i in string1:
    if i.isalpha() or i.isdigit():
        result = result + i
result = result.lower() 
print(result)      
if result == result[::-1]:
    print(True)
else: print(False)