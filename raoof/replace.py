str1=input("enter a string")
a=str1[0]
for i in str1:
    if(i==a):
        str1=str1.replace(i,'$')
        str1=a+str1[1:]
print(str1)

