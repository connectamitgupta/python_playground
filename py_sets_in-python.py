a ={1.3,5,7,9}
print(a)
print(type(a))

b={}             # this syntax will create a empty disctionary and not empty set
print(type(b))

c=set()             # this syntax will create a empty set
print(type(c))

c.add(4)
c.add(5)
c.add(8)
c.add(9)
c.add(10)
c.add(11)

print(c)
c.remove(5)
print(c)
print(len(c))
c.pop()
print(c)
#c.clear()
#print(c)

print(c.intersection({5,8}))

