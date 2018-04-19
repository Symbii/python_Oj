#!/usr/bin/env python
def maxsubarray(list):
    sum    = 0
    maxsum = list[0]
    start  = 0
    end    = 0
    for i in list:
        if sum > 0:
            sum+=i
        else:
            sum = i
            start = list.index(i)
        if maxsum<sum:
            maxsum = sum
            end = list.index(i)
    return (maxsum, start, end)

if  __name__ == '__main__':
    list=[1,2,3,4,-9,0,1,2,3,6]
    print ("maxsum=%d start=%d end=%d " % maxsubarray(list))
