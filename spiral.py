import turtle
turtle.Screen().bgcolor('red')
turtle.Screen().setup(400,400)
polygon=turtle.Turtle()
sides=50
angle=90
for i in range(sides):
    polygon.forward(i*10)
    polygon.right(angle)
turtle.done()