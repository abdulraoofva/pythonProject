rows=int(input("enter the limit"))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')