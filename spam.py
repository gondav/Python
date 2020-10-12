from time import sleep

file_input = input("File name: ")

while True:
    try:
        open_input = open(file_input)
        break
    except:
        file_input = input("File name: ")

counter = 0
sum = 0

for line in open_input:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence: '):
        counter += 1
        new_line = line[20:]
        float_number = float(new_line)
        sum += float_number

print(f"Average spam confidence: {round(sum/counter, 2)}")
