name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
mailer = dict()
mail_lst =  list()
for line in handle:
    if line.startswith('From '):
        words = line.split()
        word = words[1]
        mail_lst.append(word)

print(mail_lst)


for sender in mail_lst:
    mailer[sender] = mailer.get(sender,0) + 1
print(mailer)



big_mailer = None
big_count = None

for aaa ,bbb  in mailer.items():
    if big_mailer is None or bbb > big_count:
        big_count = bbb
        big_mailer = aaa

print(big_mailer,big_count)
