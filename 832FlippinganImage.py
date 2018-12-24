def flipimage(lst):
    """
    :type lst: List[List[int]]
    :rtype: List[List[int]]
    """
    #遍历每个小list，然后交换首尾元素。并1-0,0-1
    for each in range(len(lst)):
        i = 0
        j = len(lst[each])-1
        while i < j:
            lst[each][i], lst[each][j] = lst[each][j], lst[each][i]
            lst[each][i] = 1 - lst[each][i]
            lst[each][j] = 1 - lst[each][j]
            i += 1
            j -= 1
        #如果存在最中间的元素，不需要交换，直接1-0，0-1
        if i == j:
            lst[each][i] = 1 - lst[each][i]

    return lst

if __name__ == '__main__':
    lst = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]

    print(flipimage(lst))