import math
with open("input.txt") as f:
    a = f.readlines()
    
def solver(time, distance):
    upperbound = (time + math.sqrt(time**2 - 4*distance))/2
    upperbound = upperbound if upperbound %1 else upperbound -1
    lowerbound = (time - math.sqrt(time**2- 4*distance))/2
    return int(upperbound) - int(lowerbound)

a = [i.split(':')[1] for i in a]
#prob1
tot = 1
a = [i.strip().split() for i in a]
for i, el in enumerate(a[0]):
    (time, distance) = (int(el), int(a[1][i]))
    tot*=solver(time, distance)
print(tot)
#prob2
a = [int(''.join(i)) for i in a]
(time, distance) = (a[0], a[1])
print(solver(time, distance))

    



