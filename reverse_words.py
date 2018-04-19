#!/usr/bin/env python
import sys
def reverse_words(s):
	return '_'.join(map(lambda x:x[::-1], s.split(' ')))
if __name__ == '__main__':
	s=sys.argv
	s.pop(0)
	for x in s:
		print (reverse_words(x))
	
