from collections import deque
def accountsMerge(accounts):
    
    q = deque([])
    
    for a in accounts:
        q.append([a[0], set(a[1:])])
    
    res = []
    
    while q:
            
        curr = q.popleft()
        is_merged = False
        if curr[0] == '*':
            continue

        for item in q:
            if not curr[1].isdisjoint(item[1]):
                is_merged = True
                curr[1] |= item[1]
                item[0] = '*'
        
        if is_merged:
            q.append(curr)
        else:
            res.append(curr)
    
    ans = []
    
    for r in res:
        temp = [r[0]]
        x = list(r[1])
        x.sort()
        temp+=x
        ans.append(temp)
    return ans

accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
print(accountsMerge(accounts))