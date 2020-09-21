hours = input("Enter hours: ")
rate = input("Enter rate: ")

hours1 = float(hours)
rate1 = float(rate)
overtime = hours1 - 40

if hours1 <= 40:
    pay = hours1 * rate1
    print(f"Pay: {round(pay, 2)}")

else:
    pay = overtime * rate1 * 1.5 + 40 * rate1
    print(f"Pay: {round(pay, 2)}")

input("prompt:")
