def hammingdistance(a,b):
    temp = a ^ b
    count = 0
    while temp != 0:
        temp &= temp-1
        count+=1
    return count