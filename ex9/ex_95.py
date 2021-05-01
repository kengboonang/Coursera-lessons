fname = input("Enter file:")
if len(fname) < 1 : name = "mbox-short.txt"


fh = open(fname)
who = dict()
for line in fh:
    if not line.startswith("From ") :
        continue
    fx = line.strip()
    fy = line.split()
    dx = fy[5].split(':')
    want = dx[0]

    who[want] = who.get(want,0) + 1
x = sorted(who.items())
for items, values in x:
    print(items, values)
