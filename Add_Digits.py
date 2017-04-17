#!/usr/bin/env python
def add_digits(num):
    return num % 9 if num % 9 else 9 if num else 0
if __name__ == '__main__':
    print add_digits(11)


