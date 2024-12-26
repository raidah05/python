import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)

polygon = turtle.Turtle()

num_side = 6
len = 70
angle = 360/ num_side

for i in (num_side):
    polygon.forward(len)
    polygon.right(angle)

turtle.done()