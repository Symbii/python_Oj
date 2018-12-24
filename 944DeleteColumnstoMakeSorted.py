def minDeletionSize(A):
    """
    :type A: List[str]
    :rtype: int

    Input: ["cba","daf","ghi"]
    Output: 1
    Explanation:
    After choosing D = {1}, each column ["c","d","g"] and ["a","f","i"] are in non-decreasing sorted order.
    If we chose D = {}, then a column ["b","a","h"] would not be in non-decreasing sorted order.

    """
    if len(A) == 0:
        return 0

    columns = len(A[0])
    min_del = 0
    #锁定列, 比较每行字母的大小
    for column_index in range(columns):
        for row_index in range(len(A)-1):
            if A[row_index][column_index] > A[row_index+1][column_index]:
                min_del += 1
                break
    return min_del

if __name__== '__main__':
    lst = ["cba","daf","ghi"]
    print(minDeletionSize(lst))