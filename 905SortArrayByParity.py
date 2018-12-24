#!/usr/bin/env python

def SortArrayByParity(lst):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    evenodd_lst=[]
    for i in lst:
        if i%2 == 0:
            evenodd_lst.append(i)
    for i in lst:
        if i%2 != 0:
            evenodd_lst.append(i)
    return evenodd_lst

if __name__ == '__main__':
    lst = [3,1,2,4]
    print(SortArrayByParity(lst))