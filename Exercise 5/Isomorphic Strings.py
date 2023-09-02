def isIsomorphic(s,t):
        dic1 = {}
        dic2 = {}
        n = len(s)
        for i in range(n):
            if s[i] in dic1 or t[i] in dic2:
                if dic1.get(s[i]) != t[i] or dic2.get(t[i]) != s[i]:
                    return False
            else:
                dic1[s[i]] = t[i]
                dic2[t[i]] = s[i]
        return True

s = "egg"
t = "add"
print(isIsomorphic(s,t))