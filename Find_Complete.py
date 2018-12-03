#!/usr/bin/env python

#首先找到最高bit 1：然后构造全1，然后求差
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