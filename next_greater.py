#!/usr/bin/env python
def nextGreaterElement(num1,num2):
	cache  = {}
	temp   = []
	result = []
	for i in num2:
		while len(temp) and temp[-1]<i:
			cache[temp.pop()]=i
		temp.append(i)
	for x in num1:
		if x in cache:
			result.append(cache[x])
		else :
			result.append(-1)
	return result
if __name__=='__main__':
	num1=[2,3,4,6]
	num2=[1,2,3,7,6,4,5]
	result = nextGreaterElement(num1,num2)
	print (result)
