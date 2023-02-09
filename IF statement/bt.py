import turtle as t
import random
screen = t.Screen()
screen.setup(height=500, width=600)
guess = screen.textinput(prompt="Dự đoán con rùa nào chiến thắng?", title="Nhập vào màu rùa (đỏ, nâu, xanh dương, xanh lá cây, cam, hồng)")
colors = ["red", "brown", "blue", "green", "orange", "pink"]
y_position = [0, -30, 30, -60, 60, 90]
turtle_speed = [10, 15, 20, 25, 30, 5]
all_turtles = []
run = True
for i in range(0,6):
    turtle = t.Turtle(shape ='turtle')
    turtle.penup()
    turtle.goto(-250, y = y_position[i])
    turtle.color(colors[i])
    all_turtles.append(turtle)
def random_walk(turtle):
    global run 
    for i in turtle:
        i.forward(random.choice(turtle_speed))
        if i.xcor() >250:
            run = False
while run:
    random_walk(all_turtles)
screen.exitonclick()
