"""Unfortunately for Santa, a new Security-Elf recently started, and he has imposed some additional password requirements:

Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.
For example:

hijklmmn meets the first requirement (because it contains the straight hij) but fails the second requirement (because it contains i and l).
abbceffg meets the third requirement (because it repeats bb and ff) but fails the first requirement.
abbcegjk fails the third requirement, because it only has one double letter (bb).
The next password after abcdefgh is abcdffaa.
The next password after ghijklmn is ghjaabcc, because you eventually skip all the passwords that start with ghi..., since i is not allowed.
Given Santa's current password (your puzzle input), what should his next"""

from string import ascii_lowercase

password = "abcdefgh"


def increment_password(word):
    anti_index = 1
    letters = [x for x in word]
    while True:
        index = ascii_lowercase.index(letters[-anti_index])
        try:
            letters[-anti_index] = ascii_lowercase[index + 1]
            break
        except IndexError:
            letters[-anti_index] = "a"
            anti_index += 1
    return "".join(letters)


def has_double_pairs(word):
    i = 0
    found_pair = ""
    try:
        for x in range(i, len(word)):
            if word[x] == word[x + 1]:
                found_pair = word[x] * 2
                i = x+1
                break
        if found_pair != "":
            for x in range(i + 1, len(word)):
                if word[x] == word[x + 1]:
                    return True
    except IndexError:
        return False
    return False


def has_no_bad_letters(word):
    for x in word:
        if x in ["i", "o", "l"]:
            return False
    return True


def has_a_straight(word):
    for i, letter in enumerate(ascii_lowercase):
        three = ascii_lowercase[i:i + 3]
        if three in word:
            if len(three) == 3:
                return True
            else:
                continue
        else:
            continue
    return False


while True:
    if has_a_straight(password) and has_no_bad_letters(password) and has_double_pairs(password):
        print(f"Part 1: {password}")
        break
    else:
        password = increment_password(password)

password = increment_password(password)

while True:
    if has_a_straight(password) and has_no_bad_letters(password) and has_double_pairs(password):
        print(f"Part 2: {password}")
        break
    else:
        password = increment_password(password)
