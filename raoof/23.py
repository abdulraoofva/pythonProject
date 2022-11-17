dict={}
n=input("enter a string")

for i in n:
    if i in dict:
        dict[i]=dict[i]+1
    else:
      dict[i]=1
for m,l in dict.items():
   print(m,l)
