largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    print(num)
    try:
        inum = int(num)
    except:
        print("Invalid input")
        continue
    if smallest == None:
        smallest = inum
    elif smallest > inum:
        smallest = inum


    if largest == None:
        largest = inum
    elif largest < inum:
        largest = inum


print("Maximum is", largest)
print("Minimum is",smallest)
