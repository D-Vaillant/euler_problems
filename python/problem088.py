""" problem088.py:
        A natural number N that can be written as the sum and product of a
        given set of at least two natural numbers, {a_0, a_1, ..., a_k-1}
        is called a product-sum number:
            N= sum(a_i : i < k) = product(a_i : i < k)

        For example, 6 = 1*2*3 = 1+2+3.

        For a given set of size k, we shall call the minimal N with this
        property a minimal product-sum number. The minimal product-sum
        numbers for sets of size k=2,3,4,5,6 are as follows:
            k = 2: 4 = 2*2 = 2+2
            k = 3: 6 = 1*2*3 = 1+2+3
            k = 4: 8 = 1*1*2*4 = 1+1+2+4
            k = 5: 8 = 1*1*2*2*2 = 1+1+2+2+2
            k = 6: 12 = 1*1*1*1*2*6 = 1+1+1+1+2+6

        For 2 <= k <= 6, the sum of all the minimal product-sum numbers is
        4 + 6 + 8 + 12 = 30. 8 is only counted once.

        For 2 <= k <= 12 we have {4, 6, 8, 12, 15, 16}, with a sum of 61.

        What is the sum of all the minimal product-sum numbers for 2<=k<=12000?
"""
