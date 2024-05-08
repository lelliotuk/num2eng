import re

DIGITS = ("zero", "one", "two", "three", "four", "five", "six", "seven",
          "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen",
          "fifteen", "sixteen", "seventeen", "eighteen", "nineteen")

TENS = ("twenty", "thirty", "forty", "fifty", "sixty",
        "seventy", "eighty", "ninety", "hundred")

POW3 = ("thousand", "million", "billion", "trillion", "quadrillion",
        "quintillion", "sextillion", "septillion", "octillion", "nonillion",
        "decillion", "undecillion", "duodecillion", "tredecillion",
        "quattuordecillion", "quindecillion", "sexdecillion",
        "septendecillion", "octodecillion", "novemdecillion", "vigintillion",
        "unvigintillion", "duovigintillion", "trevigintillion",
        "quattuorvigintillion", "quinvigintillion", "sexvigintillion",
        "septenvigintillion", "octovigintillion", "novemvigintillion",
        "trigintillion", "untrigintillion", "duotrigintillion",
        "tretrigintillion", "quattuortrigintillion", "quintrigintillion",
        "sextrigintillion", "septentrigintillion", "octotrigintillion",
        "novemtrigintillion")

MAX_INT = 10**123 - 1


ORDINAL = {1: "first",
           2: "second",
           3: "third",
           5: "fifth",
           8: "eighth",
           9: "ninth",
           12: "twelfth",
           20: "twentieth",
           30: "thirtieth",
           40: "fortieth",
           50: "fiftieth",
           60: "sixtieth",
           70: "seventieth",
           80: "eightieth",
           90: "ninetieth"}

ORDINAL.update(list(map(reversed, ORDINAL.items())))

TH = ("th", "st", "nd", "rd")


def hund(num, add_and=False):
    and_used = False

    word = ""

    hun = num // 100
    modhun = num % 100
    ten = modhun // 10
    digit = num % 10

    if num >= 100:
        word += DIGITS[hun] + " hundred"
        if modhun:
            and_used = True
            word += " and "
        else:
            return word

    if num % 100 < 20:
        word += DIGITS[modhun]
    else:
        word += TENS[ten - 2]
        if digit:
            word += "-" + DIGITS[digit]
    if add_and and not and_used:
        return "and " + word
    else:
        return word


def int2eng(num, ordinal=False):
    if num < 0 or num > MAX_INT:
        raise ValueError("Integer must meet: 0 >= integer < 10^123")

    word = None
    if num < 1000:
        word = hund(num)
    elif num:
        if num % 1000:
            word = hund(num % 1000, add_and=True)
    else:
        word = hund(num)

    for i, p3 in enumerate(POW3):
        pw = 1000 ** (i + 1)
        h = num // pw % 1000
        if not h:
            continue
        if word:
            word = f"{hund(h)} {POW3[i]}, {word}"
        else:
            word = f"{hund(h)} {POW3[i]}"

    if ordinal:
        return card2ord(word)
    else:
        return word


def eng2int(num):
    num = ord2card(num)
    num = num.replace(",", " ") \
             .replace("-", " ") \
             .lower() \
             .split(" ")


    out = 0
    hund = 0

    for word in num:
        if word in DIGITS:
            hund += DIGITS.index(word)

        elif word in TENS:
            index = TENS.index(word)
            if index == 8:  # hundred
                hund = (hund or 1) * 100
            else:
                hund += (index + 2) * 10

        elif word in POW3:
            out += 1000 ** (POW3.index(word) + 1) * hund
            hund = 0

    out += hund
    return out


last_re = re.compile(r"[^-\s][a-zA-Z]+$")


def card2ord(num):  # not ideal
    last = last_re.search(num).group()
    num_int = eng2int(last)
    last = ORDINAL.get(num_int) or last + TH[0]
    out = last_re.sub(last, num)
    return out


def ord2card(num):
    num = num.lower()
    last = last_re.search(num).group()
    ord_int = ORDINAL.get(last)
    last = int2eng(ord_int) if ord_int else last.rstrip(TH[0])
    out = last_re.sub(last, num)
    return out
    

def nth(num):
    num_abs = abs(int(num))
    digit = num_abs % 10
    tens = num_abs % 100 // 10
    num = str(num)
    if digit >= 1 and digit <= 3 and tens != 1:
        return num + TH[digit]
    else:
        return num + TH[0]

