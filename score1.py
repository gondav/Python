def computegrade(score):
    if score >= 0.9:
        return "A"
    elif score >= 0.8:
        return "B"
    elif score >= 0.7:
        return "C"
    elif score >= 0.6:
        return "D"
    else:
        return "F"


input = input("Enter score: ")

try:
    score = float(input)
except:
    print("Bad score")
    quit()

if score < 0 or score > 1:
    print("Bad score")
    quit()

print("Grade:", computegrade(score))
