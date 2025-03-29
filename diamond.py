y=int(input('enter any number of rows'))
num=65

for i in range(y):
    for j in range(i+1):
        char=chr(num)
        print(char,end=' ')
        num=num+1
    print()

