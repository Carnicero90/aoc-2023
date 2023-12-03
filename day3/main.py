import re

with open("input.txt") as f:
    a = f.read().splitlines()    
#prob 1
tot = 0

for y, line in enumerate(a):
    matches = re.finditer(r"\d+", line)
    for match in matches:
        syms = []
        ran = [y-1 if y>0 else 0, (y+1 if y<len(a)-1 else y)+1]
        for  j in range(*ran):
            syms+=[i.group() for i in re.finditer(r'[^.\d]', a[j]) if i.start() <= match.end() and i.start() >= match.start()-1]
        if len(syms):
            tot+=int(match.group())
print(tot)

#prob 2
tot=0
for y, line in enumerate(a):
    multips = [m.start() for m in re.finditer('\*', line)]
    for m in multips:
        nums = []
        ran = [y-1 if y>0 else 0, (y+1 if y<len(a)-1 else y)+1]
        for  j in range(*ran):
            nums+=[int(i.group()) for i in re.finditer(r'\d+', a[j]) if i.start() <= m+1 and i.end()-1 >= m-1]
        if len(nums) == 2:
            tot+= nums[0]*nums[1]
print(tot)



