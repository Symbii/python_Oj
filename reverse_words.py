#!/usr/bin/env python
import sys
def reverse_words(s):
	return '_'.join(map(lambda x:x[::-1], s.split(' ')))
if __name__ == '__main__':
	s = "liaoxin guojiezhi"
	print (reverse_words(s))
	
