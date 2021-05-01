# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname, 'r')
list = []
for line in fh:

    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    tz = line.find("0")
    tme = line[tz:]
    tyes = float(tme)
    list.append(tyes)
all = 0
for i in list:
    all = all + i
print('Average spam confidence: ' + str(all/len(list)))
