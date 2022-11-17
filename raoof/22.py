n=int(input("enter the no of strings"))
list=[]
count=0
print("enter the strings")
for i in range(0,n):
    str=input()
    list.append(str)
print(list)
for i in list:
    for j in i:
        if(j=="a"):
            count=count+1
print("number of occurance of 'a'",count)

