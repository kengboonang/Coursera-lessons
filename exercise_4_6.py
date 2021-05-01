def computepay(h,r):
    fh = float(h)
    fr = float(r)
    if fh > 40:
        fp = fh * fr
        bh = fh - 40
        br = fr * 0.5
        pay = bh * br +  fp
    else :
        pay = fh * fr
    print("Pay " + str(pay))
    return "done"

h = input("Enter hour:")
r = input("Enter rate:")
computepay(h,r)
