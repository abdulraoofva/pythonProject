n=int(input("enter the number of element"))
list=[]
print("enter the elements")
for i in range(0,n):
    ele=int(input())
    if (ele > 100):
        list.append("over")
    else:
        list.append(ele)
print(list)

