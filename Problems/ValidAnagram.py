string1 = input()
string2= input()
from collections import Counter
if Counter(string1) == Counter(string2):
    print(True)
else:
    print(False)