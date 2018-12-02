#!/usr/bin/env python
def bubble_sort(listarry):
    for i in range(len(listarry)):
        for j in range(i, len(listarry)):
            if listarry[i] > listarry[j]:
                listarry[i], listarry[j] = listarry[j], listarry[i]
    return listarry


def select_sort(listarry):
    for i in range(len(listarry)):
        temp = i
        for j in range(i+1, len(listarry)):
            if listarry[temp] > listarry[j]:
                temp = j
        listarry[i], listarry[temp] = listarry[temp], listarry[i]
    return listarry


def quick_sort(listarry):
    if len(listarry) == 0 or len(listarry) == 1:
        return listarry
    temp = listarry[0]
    left = [i for i in listarry if i < temp]
    right = [j for j in listarry if j > temp]
    return quick_sort(left) + [temp] + quick_sort(right)


def insert_sort(listarry):
    for i in range(len(listarry)):
        j = i
        temp = listarry[i]
        while j > 0 and listarry[j-1] > temp:
            listarry[j] = listarry[j - 1]
            j -= 1
        listarry[j] = temp
    return listarry

def merge(left, right):
    i = 0
    j = 0
    newlst = []
    while i <len(left) and j < len(right):
        if left[i] > right[j]:
            newlst.append(right[j])
            j+=1
        else:
            newlst.append(left[i])
            i+=1
    if i==len(left):
        newlst.extend(right[j:])
    elif j == len(right):
        newlst.extend(left[i:])
    return newlst
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst)//2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    newlst = merge(left, right)
    return newlst


if __name__ == '__main__':
    arry = [-1, 2, 41,-3,-10,-199 ,199,4, 5, 7, 6]
    print(insert_sort(arry))
    print(quick_sort(arry))
    print(select_sort(arry))
    print(bubble_sort(arry))
    print(merge_sort(arry))
