def PeakInMountainArray1(lst):
    """
    :param lst:
    :return peakindex:
    :O(N)
    """
    return lst.index(max(lst))

def PeakInMountainArray2(lst):
    """
    :param lst:
    :return peakindex:
    :O(lgn) Binary Search
    """
    l , r = 0 , len(lst)-1
    while l < r:
        mid = (l + r) // 2
        if lst[mid]<lst[mid+1]:
            l = mid
        elif lst[mid]<lst[mid-1]:
            r = mid
        else:
            return mid

def PeakInMountainArray3(lst):
    """
    :param lst:
    :return peakindex:
    golden-section
    """
    def gold1(l, r):
        return l + int(round((r - l) * 0.382))

    def gold2(l, r):
        return l + int(round((r - l) * 0.618))

    l, r = 0, len(lst) - 1
    x1, x2 = gold1(l, r), gold2(l, r)
    while x1 < x2:
        if lst[x1] < lst[x2]:
            l = x1
            x1 = x2
            x2 = gold1(x1, r)
        else:
            r = x2
            x2 = x1
            x1 = gold2(l, x2)
    return x1