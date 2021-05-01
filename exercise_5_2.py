largest = None
smallest = None
while True:
    snum = input("Enter a number: ")
    if snum == "done":
        break
    try:
        num = float(snum)
        if largest is None:
            largest = num
        if smallest is None:
            smallest = num
        elif num > largest:
            largest = num
        elif num < smallest:
            smallest = num
    except ValueError:
        print("Invalid input")

print("Maximum is", int(largest))
print("Minimum is", int(smallest))
