import math


def farey_sequence(n):
    farey_seq = [[0, 1], [1, 1]]

    for denominator in range(2, n + 1):
        for numerator in range(1, denominator):
            if math.gcd(numerator, denominator) == 1:
                farey_seq.append([numerator, denominator])

    farey_seq.sort(key=lambda x: x[0] / x[1])

    return farey_seq


n = 2
sequence = farey_sequence(n)
print(n, ":", sequence)
