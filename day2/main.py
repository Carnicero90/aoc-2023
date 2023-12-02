import re
from math import prod

with open("input.txt") as f:
    a = f.readlines()

#prob 1
regex= "(1[3-9]|[2-9][0-9]) r|( 1[4-9]|[2-9][0-9]) g|( 1[5-9]|[2-9][0-9]) b"
b = [int(i.split(" ")[1].strip(":")) for i in a if not re.search(regex, i)]

print(sum(b))

#prob 2
regex2 = r'(\d*) ([rbg])'
tot = 0
for i in a:
    nums = {
            'r': 0,
            'g': 0,
            'b': 0,
            }

    el  = re.findall(regex2, i)

    for i in el:
        if (int(i[0]) > nums.get(i[1], 0)):
            nums[i[1]] = int(i[0])

    tot+=prod(nums.values())

print(tot)

