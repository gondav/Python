from time import sleep
# prompt the user to provide an integer between 1 and 8

#def main():
while True:
    strput = input("Enter a positive integer from 1 to 8: ")

    try: intput = int(strput)
    except: continue

    if intput < 1 or intput > 8:
        continue

    if intput >=1 and intput<=8:
        break

j = 1

for i in reversed(range(intput)):
    print(" " * i, end="") ; sleep(1)
    print("#" * j, "#" * j, end="")
    print()
    j += 1
    
        
