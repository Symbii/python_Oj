**Python_Leetcode_Oj**
----------------------
* Keyboard row

```python
line1, line2, line3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
ret = []
for word in words:
    w = set(word.lower())
    if w.issubset(line1) or w.issubset(line2) or w.issubset(line3):
        ret.append(word)
```

* Reverse_words
```python
' '.join(map(lambda x:x[::-1],s.split()))
```

* Next greater element
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
* Find Max Consective Ones
```python
for x in nums:
    if x==1:
    counts=counts+1
elif x==0:
	counts=0
if maxcounts<counts:
	maxcounts=counts
return maxcounts
``` 
