hrs = input("Enter Hours:")
h = float (hrs)
rate = input("Enter rate:")
r = float (rate)
pay = h * r
if h > 40:
    bonus = h - 40
    bonus_pay = (40 * r) + bonus * (1.5 * r)
    print(bonus_pay)
