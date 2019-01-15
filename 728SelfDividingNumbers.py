def isDividing(val):
    """
    :param val:
    :return True or False:
    """
    temp_val = val
    #遍历数中的每位数字
    while val>0:
        m = val % 10
        #每位上的数字为0或者不能整除返回false
        if m is 0 or temp_val % m is not 0:
            return False
        val//= 10
    return  True

def SelfDividingNumber(left,right):
    """
    :param left:
    :param right:
    :return list[]:
    """
    result = list()
    #遍历整个left和right之间的所有数字：
    while left <= right:

        #判断每个数字是否是DivdingNumer
        if isDividing(left):
            result.append(left)
        left += 1
    return result
