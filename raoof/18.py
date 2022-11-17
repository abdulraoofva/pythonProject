d={3:4,2:1,1:5}
x=sorted(d.items())
print(x)

y=sorted(d.keys())
print(y)
z=sorted(d.values())
print(z)
m=sorted(d.items(),reverse=True)
print("the decending order is",m)
n=sorted(d.keys(),reverse=True)
print("decending order keys",n)
o=sorted(d.values(),reverse=True)
print(o)