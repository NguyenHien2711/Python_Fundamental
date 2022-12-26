import turtle
import random
import time
screen = turtle.Screen()
screen.bgcolor('lightblue')
player_one = turtle.Turtle()
player_one.color('blue')
player_one.shape('turtle')
player_two = player_one.clone()
player_two.color('red')
#Position players
player_one.penup()
player_one.goto(-300, 200) 
player_two.penup()
player_two.goto(-300,-200) 
#Draw a finish line
player_one.goto(300, -250)
player_one.left(90)
player_one.pendown()
player_one.color('black') #change color of line to black
player_one.forward(500)
player_one.write('Finish!', font=24)
player_one.penup()
player_one.goto(-300, 200)

player_one.pendown()
player_two.pendown()

die = [i for i in range(1,7,1)]
for i in range(30):
    if player_one.pos() >=(300,250):
        print('Player One wins the race')
        break
    elif player_two.pos() >=(300,-250):
        print('Player Two wins the race')
        break
    else:
        die_roll1 = random.choice(die)
        player_one.forward(30*die_roll1)
        time.sleep(2)
        die_roll2 = random.choice(die)
        player_two.forward(30*die_roll2)
        time.sleep(2)
    
turtle.done() 