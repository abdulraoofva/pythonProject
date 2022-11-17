str1=input("enter a string")
dict={}
word=str1.split(" ")
print(str1)
for i in word:
    if i in dict:
      dict[i]=dict[i]+1
    else:
        dict[i]=1
for m,n in dict.items():
  print(m,n)
