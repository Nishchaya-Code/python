sci=int(input('enter science marks'))
maths=int(input('enter maths marks'))
eng=int(input('enter english marks'))
  
avg=(sci+maths+eng)/3
print(avg)

if avg>=90:
    print('A')
elif avg>=75 and avg<90:
    print('B')
elif avg>=50 and avg<75:
    print("C")
else:
    print("F")