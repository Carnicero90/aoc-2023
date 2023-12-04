with open("input.txt") as f:
    a = f.readlines()

middle = a[0].find('|')
maxlen = len(a)
tot = 0
stack=[1 for i in range(maxlen)]

for i, line in enumerate(a):
    matches = len(set(line[8:middle].split()).intersection(line[middle:].split()))  
    tot+=2**(matches-1) if matches else 0
    for j in range(i+1, i+matches+1):
        if(j <maxlen):
            stack[j]+=stack[i]
# prob 1
print(tot)
# prob 2
print(sum(stack))



    



