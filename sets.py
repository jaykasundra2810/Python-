s = set([1,2,3,4,5])
print(s)
s.add(6)
s.add(7)
print(s)
s.remove(7)
print(s)
s.union((6,7))
#print(s.union((6,7))
print(s.intersection((2,3,4,8)))
print(len(s))
print(max(s))
print(min(s))

