fname = input("Enter file:")
if len(fname) < 1 : name = "mbox-short.txt"


fh = open(fname)
who = dict()
for line in fh:
    if not line.startswith("From ") :
        continue
    fx = line.strip()
    fy = line.split()
    for f in fy:

        who[f] = who.get(f,0) + 1
        #print(f,who[f])

largest = -1
word = None
for k,v in who.items() :
    if v < 6:
        if v > largest :
            largest = v
            word = k

print(word,largest)


        #oldcount = who.get(f,0)
        #newcount = oldcount + 1
        #who[f] = newcount
        #print(f,newcount)


        #(if f in who:
            #who[f] = who[f] + 1
        #else:
            #who[f] = 1
        #print(f, who[f])
