# import turtle
# t = turtle.Turtle()
# t.hideturtle()
# t.penup()
# t.goto(0, -50)
# t.pendown()
# d = 50
# k = 0 
# while 1:
#     t.circle(d, 180)
#     d = (2*d+d/2)/2
#     t.circle(d, 180)
#     k+=1
#     if k ==10:
#         break 
# turtle.done()
import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Star")

myPen = turtle.Turtle()
myPen.speed(0)
myPen.color("#FF0000")

for j in range (1,100):
    for i in range (1,6):
        myPen.left(144)
        myPen.forward(200)
    myPen.left(5)

turtle.done()