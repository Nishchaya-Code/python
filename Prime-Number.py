lower=int(input('input lower range'))
u=int(input('input upper range'))
for i in range(lower, u+1):
    if i>1:
        for j in range(2, i):
            if i%j==0:
                break
        else:
            print(i)