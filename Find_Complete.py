#!/usr/bin/env python

def find_complete(num):
    tmp = num
    maxbits = 0
    while tmp != 0:
        tmp = tmp >> 1
        maxbits += 1
    sum = 0
    for i in range(maxbits):
        sum |= 1<<i

    return sum - num

if __name__ == "__main__":
    print(find_complete(9))