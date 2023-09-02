def groupAnagrams(strs):
    d = {}
    for i in strs:
        res = "".join(sorted(i))
        if res not in d:
            d[res] = [i]
        else:
            d[res].append(i)
    return d.values()

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))