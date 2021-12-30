fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
for every_line in fh:
    every_line = every_line.rstrip()
    if every_line.startswith('From '):
        email = every_line.split()
        print(email[1])
        count += 1


print("There were" ,count, "lines in the file with From as the first word")
