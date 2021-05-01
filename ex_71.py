# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname,'r')
fr = fh.read().rstrip().upper()
print(fr)
