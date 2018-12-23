def ReapetedNtimes(lst):
    #sort lst
    lst.sort()

    counts = len(lst)

    mid = counts//2

    if lst[mid] == lst[mid-1]:
        return lst[mid]
    elif lst[mid-1] == lst[0]:
        return lst[0]
    else:
        return lst[counts-1]


if __name__ == '__main__':
    lst = [1,1,1,1,2,2,2,4]
    print(ReapetedNtimes(lst))