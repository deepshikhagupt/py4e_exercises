name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

hours = dict()
for line in handle:
    if line.startswith('From '):
        phrase = line.split()
        for words in phrase:
            word = phrase[5].split(':')
            hour = word[0]
        hours[hour] = hours.get(hour , 0) + 1


lst = list()
for key , val in hours.items():
    new_tup = key , val
    lst.append(new_tup)

new_lst = sorted(lst)

for val , key in new_lst:
    print (val , key)

#print(sorted((v,k) for (k,v) in hours.items()))
