#!/usr/bin/env python
__author__= "liaoxin"
def FindMaxConsecutiveOnes(nums):
    counts=0
    maxcounts=0
    for x in nums:
        if x==1:
            counts=counts+1
        elif x==0:
            counts=0
        if maxcounts<counts:
            maxcounts=counts
    return maxcounts
if __name__ == '__main__' :
    print FindMaxConsecutiveOnes([1,1,1,0,1,0,1,1])
