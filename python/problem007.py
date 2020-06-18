""" problem7.py
        Find the 10,001st prime number.
"""

prime_count = 1
prime_list = [2]

i = 2
while prime_count < 10001:
    i += 1
    if any(i%p == 0 for p in prime_list):
        continue
    else:
        prime_list.append(i)
        prime_count += 1

print(prime_list[-1])
