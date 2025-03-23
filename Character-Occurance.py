w=input('input any word')
c=input('what characters do you want to find in the word')
count=0
for i in w:
    if i==c:
        count+=1
print(count)