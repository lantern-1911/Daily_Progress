num = int(input())
d = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100:'C',
        400:'CD',
        500:'D',
        900:'CM',
        1000:'M',
    }
useOnce = {4,9,40,90,400,900}
res = []
for key in reversed(d.keys()):
    times = num // key
    if key not in useOnce or times==1:
        res += [d[key]]*times
        num -= key*times
print(''.join(res))        