#!/usr/bin/env python
import string
import sys
import traceback
def findwords(list):
    res=[]
    flag=1
    dict={'q':1,'w':1,'e':1,'r':1,'t':1,'y':1,'u':1,'i':1,'o':1,
          'a':2,'s':2,'d':2,'f':2,'g':2,'h':2,'j':2,'k':2,'l':2,
          'z':3,'x':3,'c':3,'v':3,'b':3,'n':3,'m':3}
    for k in list:
        temp = k.lower()
        for i,j in enumerate(temp):
            if len(temp) != 1:
                try:
                    if i<len(temp)-1 and dict[temp[i]] != dict[temp[i+1]]:
                        flag=0
                        break
                    elif i<len(temp)-1 and dict[temp[i]] == dict[temp[i+1]]:
                        flag=1
                except:
                    traceback.print_exc()
                    return
            else:
                flag = 1
        if flag==1:
            res.append(k)
    return res
if __name__ == '__main__':
    list = sys.argv
    list.pop(0)
    res = findwords(list)
    print res
