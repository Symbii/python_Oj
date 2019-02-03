def sortbyparity(lst):
    '''
    :param nums: list[]
    :return: list[]
    '''
    ret_lst = list()
    even_idx = 0
    odd_idx = 1
    for i in A:
        if i % 2 == 0:
            ret_lst.insert(even_idx, i)
            even_idx += 2
        else:
            ret_lst.insert(odd_idx, i)
            odd_idx += 2
    return ret_lst