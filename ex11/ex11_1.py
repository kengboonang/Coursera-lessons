# import re
# f = input()
# numlist = list()
# count = 0
# g = open(f, 'r')
# for line in g:
#     gx = line.strip().split()
#     for g in gx:
#
#         gw = re.findall('([0-9]+)', g)
#         if len(gw) == 0: continue
#         for el in gw:
#             gwa = int(el)
#             numlist.append(gwa)
#             count = count+1
#
# print(numlist)
# print(count)
# print(sum(numlist))

#Shorterning code attempt 1
#
# import re
# f = input()
# total = 0
# g = open(f, 'r')
# for line in g:
#     g = line.strip()
#     gw = re.findall('([0-9]+)', g)
#     if len(gw) == 0: continue
#     for el in gw:
#         gwa = int(el)
#         total = total + gwa
#
# print(total)
#



import re
print(sum( [ ??? in input().findall('[0-9]+', input().read())]))
