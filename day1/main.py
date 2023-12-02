import re

with open("input.txt") as f:
    inp = f.read().strip()

#prob 1
regex = '(?:.*?)((([1-9]).*(?=)([1-9]).*)|([1-9]).*)'
sub = r'\g<3>\g<4>\g<5>\g<5>'
p = re.sub(regex, sub, inp)
print(eval(re.sub('\n', '+', p)))

#prob 2
chars = 'one|two|three|four|five|six|seven|eight|nine'
regex = rf'(?:.*?)((({chars}|[1-9]).*(?=)({chars}|[1-9]).*)|({chars}|[1-9]).*)'
p = re.sub(regex, sub, inp)
pattern = '|'.join(f'({s})' for s in chars.split('|'))+'|(\n)'
rep = lambda m: str(m.lastindex) if m.lastindex < 10 else '+'
print(eval(re.sub(pattern, rep, p)))
