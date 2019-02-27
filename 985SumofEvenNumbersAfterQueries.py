def sumofevenafterquery(lst, querylst):
    '''
    :param lst: lst[int]
    :param querylst: lst[lst[int]]
    :return: lst[int]
    '''
    # return lst
    result = list()

    # 初始sum
    s = sum(x for x in lst if x % 2 == 0)

    # 遍历querylst
    # 如果是偶数的项就原sum就先减去 ，如果计算完还为偶数，就加回来，
    # 如果是奇数的项，就看计算后为偶数的话,直接加回来
    for i in range(len(querylst)):

        # 判断修改的项，初始是否为even
        if lst[querylst[i][1]] % 2 == 0:
            s -= lst[querylst[i][1]]

        # 计算更新
        lst[querylst[i][1]] += lst[querylst[i][0]]

        # 判断计算之后的值是否为even
        if lst[querylst[i][1]] % 2 == 0:
            s += lst[querylst[i][1]]

        result.append(s)

    return result