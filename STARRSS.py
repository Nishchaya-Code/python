import turtle
turtle.Screen().bgcolor('red')
turtle.Screen().setup(400,400)
polygon=turtle.Turtle()
sides=3
angle=360/sides
for i in range(sides):
    polygon.forward(100)
    polygon.left(angle)
polygon.penup()
polygon.left(90)
polygon.forward(50)
polygon.right(90)
polygon.pendown()
for i in range(sides):
    polygon.forward(100)
    polygon.right(angle)
turtle.done()