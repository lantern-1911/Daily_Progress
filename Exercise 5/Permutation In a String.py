def checkInclusion(s1,s2):
        s_ls = list(s1)
        i = 0        
        while i < (len(s2) - len(s1) + 1):
            j = 0
            while j < len(s1):
                if s2[i + j] in s_ls:
                    s_ls.remove(s2[i + j])
                    j += 1
                else:
                    if s2[i + j] in s1:
                        i += s2[i:].index(s2[i + j]) + 1
                    else:
                        i += 1
                    s_ls = list(s1)
                    break
            else:
                return True
        return False

s1 = "dcccefbali"
s2 = "ab"
print(checkInclusion(s1,s2))