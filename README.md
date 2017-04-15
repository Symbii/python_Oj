**# python_Leetcode_oj**
*keyboard_row

```python
line1, line2, line3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
ret = []
for word in words:
	w = set(word.lower())
	if w.issubset(line1) or w.issubset(line2) or w.issubset(line3):
		ret.append(word)
```

*reverse_words
```python
' '.join(map(lambda x:x[::-1],s.split()))
```

*next_greater_element
```python  	
for i in num2:
    while len(temp) and temp[-1]<i:
        cache[temp.pop()]=i
    temp.append(i)
for x in num1:
    if x in cache:
        result.append(cache[x])
    else :
        result.append(-1)
```
