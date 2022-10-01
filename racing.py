import turtle
import time
import random

turtle.bgcolor('black')
turtle.title('Перегонки')

f=turtle.Turtle()
f.speed(0)
f.color('white')
f.penup()
f.goto(240,240)
f.write("Finish", font=("Arial", 20, "bold"))
f.penup()
f.goto(280,220)
f.pendown()
f.goto(280,-250)
f.hideturtle()

yellow =turtle.Turtle()
yellow.shape('turtle')
yellow.color('yellow')
yellow.pensize(10)
yellow.penup()
yellow.goto(-300,150)
yellow.pendown()

red =turtle.Turtle()
red.shape('turtle')
red.color('red')
red.pensize(10)
red.penup()
red.goto(-300,0)
red.pendown()

green =turtle.Turtle()
green.shape('turtle')
green.color('green')
green.pensize(10)
green.penup()
green.goto(-300,-150)
green.pendown()

text =turtle.Turtle()
text.color('white')
text.penup()
text.goto(-300,240)
text.hideturtle()

for i in range(3):
    text.write(3-i,font=("Arial", 20, "bold"))
    time.sleep(1)
    text.clear()

text.write('Start',font=("Arial", 20, "bold"))


first=random.choice(['yellow','red','green'])

def end():
    if yellow.position()[0]>=280:
        text.clear()
        text.color('yellow')
        text.write('Yellow WIN',font=("Arial", 20, "bold"))
        return True
    if red.position()[0]>=280:
        text.clear()
        text.color('red')
        text.write('Red WIN',font=("Arial", 20, "bold"))
        return True
    if green.position()[0]>=280:
        text.clear()
        text.color('green')
        text.write('Green WIN',font=("Arial", 20, "bold"))
        return True
    return False

while True:
    if first=='yellow':
        yellow.forward(random.randint(1,50))
        if end():break
        red.forward(random.randint(1,50))
        if end():break
        green.forward(random.randint(1,50))
        if end():break
    elif first=='red':
        red.forward(random.randint(1,50))
        if end():break
        green.forward(random.randint(1,50))
        if end():break
        yellow.forward(random.randint(1,50))
        if end():break
    else:
        green.forward(random.randint(1,50))
        if end():break
        yellow.forward(random.randint(1,50))
        if end():break
        red.forward(random.randint(1,50))
        if end():break
    time.sleep(0.5)






