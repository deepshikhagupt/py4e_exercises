import re
name = input("Enter file:")
if len(name) < 1:
    name = "regex_sum_1283199.txt"
handle = open(name)
lst = list()
sum = 0
for line in handle:
    line = line.rstrip()
    x = re.findall('[0-9]+',line)
    for i in range(len(x)):
        c = int(x[i])
        sum += c


print(sum)
