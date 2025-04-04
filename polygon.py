import turtle
turtle.Screen().bgcolor('red')
turtle.Screen().setup(400,400)
polygon=turtle.Turtle()
sides=6
angle=360/sides
for i in range(sides):
    polygon.forward(69)
    polygon.right(angle)
turtle.done()