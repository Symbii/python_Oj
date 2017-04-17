#!/usr/bin/env python
def finddiff(s,t):
    slist=list(s)
    tlist=list(t)
    slist.sort()
    tlist.sort()
    for x in slist:
        tlist.pop(tlist.index(x))
    return ''.join(tlist)
if __name__ == '__main__':
     print finddiff("abcd","abcdef")