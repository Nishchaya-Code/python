y=int(input('enter any number of rows'))
num=1

for i in range(y):
    for j in range(i+1):
        print(num,end=' ')
        num=num+1
    print()

