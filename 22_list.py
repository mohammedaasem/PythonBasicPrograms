# copy()
# Different between b=a & b=a.copy() with clear()

a=[10,20]
b=a
print(type(a))
print(type(b))
print(a)
print(b)

a.clear()
print(a)
print(b)

c=[1,2]
d=c.copy()
print(c)
print(d)

c.clear()
print(c)
print(d)
