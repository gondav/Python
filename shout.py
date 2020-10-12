fopen = open("mbox.txt")
shout = fopen.read()

for line in shout:
    print(line.upper(), end="")


fopen.close()
