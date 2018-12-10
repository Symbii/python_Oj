#!/usr/bin/env python

def Find_Anagram(lst1, lst2):
    return [lst2.index(x) for x in lst1]

if __name__=='__main__':
    lst1 = [1,2,3,4]
    lst2 = [5,4,2,3,1]
    print(Find_Anagram(lst1,lst2))