# -*- coding: utf-8 -*-

'''
Problem44 「Pentagon numbers」

Pentagonal numbers are generated by the formula, P(n)=n(3n−1)/2. The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P(4) + P(7) = 22 + 70 = 92 = P(8). However, their difference, 70 − 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, P(j) and P(k), for which their sum and difference are pentagonal and D = |P(k) − P(j)| is minimised; what is the value of D?
(五角数P(n)について、和も差も五角数となりその差の絶対値が最小となるP(j), P(k)の組を見つけ、その差の絶対値Dを求めよ。)
'''

import time

def find_d():
    pentagon_numbers = []
    n = 1
    while True:
        p_k = n * (3*n - 1) / 2
        for p_j in pentagon_numbers[::-1]:
            if (((1 + 24 * (p_k + p_j)) ** 0.5 + 1) / 6).is_integer() and (p_k - p_j) in pentagon_numbers:
                return int(p_k - p_j)
        pentagon_numbers.append(p_k)
        n += 1


if __name__ == '__main__':
    start = time.time()

    print(find_d()) # answer 5482660

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 0.46048sec
