def lookup(value):
    switcher = {
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


def num_to_words(number):
    result = ""    
    if number >= 1000:
        thousands, number = divmod(number % 10000, 1000)
        result += lookup(thousands) + "thousand"
    
    if number >= 100:
        hundreds, number = divmod(number % 1000, 100)
        connector = "and" if number > 0 else ""
        result += lookup(hundreds) + "hundred" + connector
    
    if number < 20:
        result += lookup(number)
    else:
        tens, digits = divmod(number % 100, 10)
        result += lookup(tens * 10) + lookup(digits)

    return result


total = 0
for x in range(1, 1001):
    total += len(num_to_words(x))

print(total)