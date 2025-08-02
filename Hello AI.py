print("Hello my name is AIV1. What's your name?")
name=input()
print(f"Hello {name}, nice to meet you")

print("How are you feeling today? (good|bad)")
feeling1=input().lower()
if feeling1=='good':
    print("That's great! You must be having a good day")
elif feeling1=="bad":
    print("I'm sorry hope you get better")
else :
    print("It's ok if you don't want to tell me")

print(f"Good bye {name} hope you have a nice day")