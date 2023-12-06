import re
import math

with open("input.txt") as f:
    a = f.read()
a = a.replace('\n\n', '\n')
a = re.sub(r'[^\d :\n]+', '', a)
a = a.split(':')[1:]
a = [i.strip().split('\n') for i in a]
seeds = [int(i) for i in a.pop(0)[0].split()]
a = [[j.split() for j in i] for i in a]
a = reversed([[[int(j) for j in i] for i in k] for k in a])
news = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds),2)]
for i in range(0,len(seeds),2):
    news.append((seeds[i:i+2]))
seed = 0
prob1 = 0
prob2 = 0
while(not prob2 or not prob1):
    if (seed > 265018614):
        print('errai')
        break
    current = seed
    for el in a:
        match = next((x for x in el if x[0]<=current and x[0]+x[2]>=current), False)
        current = current+match[1]-match[0] if match else current

    if current in seeds and not prob1:
        prob1 = seed
    for i in news:
        if (current>=i[0] and current<=i[0]+i[1]) and not prob2:
            prob2 = seed    
    seed+=1
#prob1
print(prob1)
#prob2
print(prob2)