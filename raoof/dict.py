dict1={'fruit':'apple','climate':'cold','price(kg)':120}
print(dict1)
print(dict1['fruit'])
dict1.pop('fruit')
print(dict1)
dict1.update({'climate':'hot'})
dict1.update({'fruit':'orange'})
print(dict1)
x=dict1.copy()
print(x)
y=dict1.keys()
print(y)
z=dict1.values()
print(z)
m=dict1.items()
print(m)