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
            if listarry[i] > listarry[j]:
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

if __name__ == '__main__':
    arry = [1, 2, 3, 4, 5, 7, 6]
    print(insert_sort(arry))
    print(quick_sort(arry))
    print(select_sort(arry))
    print(bubble_sort(arry))
