import re
f = input()
numlist = list()
count = 0
g = open(f, 'r')
for line in g:
    gx = line.strip().split()
    for g in gx:

        gw = re.findall('([0-9])+', g)
        if len(gw) != 1: continue
        gwa = int(gw[0])
        numlist.append(gwa)
        count = count+1
print(numlist)
print(count)
print(sum(numlist))
