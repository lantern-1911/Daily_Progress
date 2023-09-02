from collections import Counter
def leastInterval(tasks, n):
    if not n:return len(tasks)
    counter = Counter(tasks)
    counter = Counter(counter.values())
    maxkey = max(counter.keys())
    total = len(tasks) - counter[maxkey]
    return counter[maxkey] + ((maxkey-1)*(n+1) if total <= (maxkey-1)*(n+1) else total)

tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2
print(leastInterval(tasks,n))

        