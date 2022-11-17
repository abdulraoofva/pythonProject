def factor(num):
    for i in range(1,num+1):
        if(num%i==0):
            print(i)
num=int(input("enter the number"))
print("the factors of the numbers are")
factor(num)




