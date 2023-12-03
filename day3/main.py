import re

with open("input.txt") as f:
    a = f.read().splitlines()

def solver(regex1, regex2, callback):
    tot = 0
    for y, line in enumerate(a):
        matches = re.finditer(regex1, line)
        for match in matches:
            results = []
            ran = [y-1 if y>0 else 0, (y+1 if y<len(a)-1 else y)+1]
            for  j in range(*ran):
                results+=[i.group() for i in re.finditer(regex2, a[j]) if i.start() <= match.end() and i.end() >= match.start()]
            tot+=callback(results, match)
    print(tot)
#prob 1
solver(r"\d+", r"[^.\d]", lambda results, match: int(match.group()) if len(results) else 0)
#prob 2
solver(r"\*", r"\d+", lambda results, match: int(results[0])*int(results[1]) if len(results) == 2  else 0)



