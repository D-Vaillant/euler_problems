""" problem017.py:
        If the numbers 1 to 5 are written out in words: one, two, three, four,
        five, then there are 3+3+5+4+4 = 19 letters used in total.

        If all the letters from 1 to 1000 inclusive were written out in words,
        how many letters would be used?

        Spaces and hyphens are not letters.
        342 = Three Hundred and Forty-Two => 23 letters
        115 = One Hundred and Fifteen => 20 letters.
"""

atomics = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven",
           8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen",
           14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen",
           19:"nineteen", 20:"twenty", 30:"thirty", 40:"forty", 50:"fifty",
           60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety",
           1000:"onethousand", 0:"zero"}

def num2word(x):
    if x in atomics:
        return atomics[x]
    else:
        if x < 100:
            return num2word((x//10)*10) + num2word(x%10)
        else:
            a = x % 100
            if a:
                return "{}hundredand{}".format(num2word(x//100),num2word(a))
            else:
                return "{}hundred".format(num2word(x//100))

if __name__ == "__main__":
    assert(len(num2word(342)) == 23)
    assert(len(num2word(115)) == 20)

    print(sum(len(num2word(x)) for x in range(1, 1001)))
