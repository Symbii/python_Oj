#!/usr/bin/env python

import collections
def Subarray_Sum2(lst, s):
    '''
    说是什么前缀0，可是prefix记录的还是每个1之间0的个数，所以以s=2为例，第7个1时候，只需要统计第5个1里面记得个数，每当第7个1后面多一个0，
    变多加一次第5个1里面的个数。即：X(I)表示lst里面所有为1的元素,I表示第几个1,  SUM[X(6), X(7)] = S = 2,
    种类 就等于Cnt = SUM(0):[X(5),X(6)] * SUM(0)[X(7), X(8)]
    '''
    sum = 0
    ret = 0
    prefix= collections.Counter({0:1})
    for x in lst:
        sum += x
        ret += prefix[sum-s] #将[X(5),X(6)] + [X(5),X(6)] 按照0的个数执行即 Cnt = SUM(0):[X(5),X(6)] * SUM(0)[X(7), X(8)]
        prefix[sum] += 1
    return ret

def Subarray_Sum(lst, s):

    num = 1
    zero_cnt=[]

    # 计算每个1之前有num-1个0,得到一个新列表
    for i in lst:
        if i == 1:
            zero_cnt.append(num)
            num = 1
        else:
            num += 1
    zero_cnt.append(num)
    # 计算
    cnt = 0
    if s == 0:
        #计算每个1之间的0的个数,x个0就有1，2，3，...,x种，等差数列求和
        for x in zero_cnt:
            cnt += (x*(x-1))
        cnt //= 2
    else:
        #计算第i 个1和 第i+s 个 1各自之前的0的个数 相乘。
        #for L,R in zip(zero_cnt, zero_cnt[s:]):
        #    cnt += L*R
        for i in range(len(zero_cnt)):
            if(i+s < len(zero_cnt)):
                cnt += zero_cnt[i] * zero_cnt[i+s]
    return  cnt

if __name__ == "__main__":
    pass