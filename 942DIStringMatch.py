def DI_String_Match(str):
    '''
    :param str: string
    :return: list
    example:
        Input: "IDID"
        Output: [0,4,1,3,2]
    '''

    temp = []
    result = []

    #构造[0....N] list
    for i in range(len(str)+1):
        temp.append(i)

    # 遇到D就放当前最大的，遇到I就放当前最小的
    for i in str:
        if i == 'I':
            result.append(temp.pop(0))
        elif  i == 'D':
            result.append(temp.pop())

    #最后一个元素直接放进去就ok
    result.append(temp.pop())
    return result


