fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    single = line.rstrip()
    single = line.split()
    for word in single:
        if word in lst:
            continue
        else:
            lst.append(word)

print(sorted(lst))
