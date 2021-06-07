from cs50 import get_string

def main():

    text = get_string("Text: ")
    result = round(coleman_liau_index(text))

    if result < 1:
        print("Before Grade 1")
    elif result >= 16:
        print("Grade 16+")
    else:
        print("Grade", result)


# Coleman-Liau index is computed as 0.0588 * L - 0.296 * S - 15.8
def coleman_liau_index(txt):
    words = len(txt.split())
    letters = 0
    sentences = 0
    for c in txt:
        if c.isalpha():
            letters += 1
        if c in ['.', '!', '?']:
            sentences += 1

    l = 100 / words * letters
    s = 100 / words * sentences
    index = 0.0588 * l - 0.296 * s - 15.8

    return index

main()