def toWord(value):
    switcher = {
        0: "",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety"
    }
    return switcher.get(value, "")


def toWords(number):
    result = toWord(number)
    if result != "":
        return result

    text = str(number)    

    hundreds = int(text[len(text)-3]) if number >= 100 else 0
    thousands = int(text[len(text)-4]) if number >= 1000 else 0

    remaining = number % 100
    
    if thousands > 0:
        result += toWord(thousands) + 'thousand'

    if hundreds > 0:
        result += toWord(hundreds) + 'hundred'
        if remaining > 0:
            result += "and"

    if remaining > 0:
        remaining_result = toWord(remaining)
        if remaining_result != "":
            result += remaining_result
        else:
            ones = remaining % 10
            tens = remaining - ones

            if tens > 0:
                result += toWords(tens)
            
            if ones > 0:
                result += toWord(ones)

    return result

total = 0
for x in range(1, 1001):
    print(toWords(x))
    total += len(toWords(x))

print(total)