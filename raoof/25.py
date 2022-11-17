list1=[]
n=int(input("enter the number of elements"))
for i in range(0,n):
    i=input()
    list1.append(i)
print(list1)
list2=[]
m=int(input("enter the number of elements in list 2"))
for i in range(0,m):
    i=input()
    list2.append(i)
print(list2)
print("colours present in list 1 but not in list 2 are")
a=list(set(list1).difference(list2))
print(a)