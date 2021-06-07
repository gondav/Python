from cs50 import get_string

def main():

    cred_num = get_string("Number: ")
    if luhns_algorithm(cred_num):
        print(first_two_digits(cred_num))
    else:
        print("INVALID")

def first_two_digits(num):

    length = len(num)
    digit = num[0]
    digits = num[:2]

    # American Express uses 15-digit numbers; All American Express numbers start with 34 or 37
    if length == 15 and (digits == '34' or digits == '37'):
        return 'AMEX'
    # MasterCard uses 16-digit numbers; MasterCard numbers start with 51, 52, 53, 54, or 55
    elif length == 16 and digits in ['51', '52', '53', '54', '55']:
        return 'MASTERCARD'
    # Visa uses 13- and 16-digit numbers; Visa numbers start with 4
    elif (length == 13 or length == 16) and digit == '4':
        return 'VISA'
    else:
        return 'INVALID'

def luhns_algorithm(num):

    #num = int(num)
    multiply, total = 0, 0
    # Multiply every other digit by 2, starting with the number’s second-to-last digit, and then add those products’ digits together.
    for i in range(len(num) - 2, - 1, -2):
        multiply = int(num[i]) * 2
        if multiply < 10:
            total += multiply
        else:
            total += (multiply - 9)
    #Add the sum to the sum of the digits that weren’t multiplied by 2
    for i in range(len(num) - 1, - 1, -2):
        total += int(num[i])
    # If the total’s last digit is 0 (or, put more formally, if the total modulo 10 is congruent to 0), the number is valid!
    if total % 10 == 0:
        return True
    else:
        return False
    return total

main()