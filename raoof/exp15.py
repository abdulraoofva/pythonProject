list1=[12,34,65,-7,5]
list2=[13,64,37,-6,5]
x=len(list1)
y=len(list2)
a=sum(list1)
b=sum(list2)
if(x==y):
    print("they are of same length")
else:
    print("not same")
print("the common elements")
for i in list1:
    for j in list2:
        if(i==j):
            print(i)



