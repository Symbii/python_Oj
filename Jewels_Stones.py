#!/usr/bin/env python


def JewelsStones(j,s):
    count = 0
    for jindex, jvalue in enumerate(j):
        for sindex , svalue in enumerate(s):
            if jvalue == svalue:
                count += 1
    return count



if __name__ == '__main__':
    print(JewelsStones("aA","AAAAAAAA"))