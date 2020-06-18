""" problem022.py:
        Using names.txt (right click and 'Save Link/Target As...'), a 46K text
        file containing over five-thousand first names, begin by sorting it
        into alphabetical order. Then working out the alphabetical value for
        each name, multiply this value by its alphabetical position in the list
        to obtain a name score.

        For example, when the list is sorted into alphabetical order, COLIN,
        which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the
        list. So, COLIN would obtain a score of 938  53 = 49714.

        What is the total of all the name scores in the file?
"""

def letter_to_num(letter):
    return ord(letter) - ord('A') + 1

def word_to_num(word):
    return sum(map(letter_to_num, word))

def read_names():
    # This really just takes all the fun out of the problem...
    with open("p022_names.txt") as pw:
        r = pw.read().split(',')
    return sorted(list(map(lambda x: x.strip('"'), r)))

if __name__ == "__main__":
    out = 0
    for index, name in enumerate(read_names()):
        out += (index + 1) * (word_to_num(name))
    print(out)

