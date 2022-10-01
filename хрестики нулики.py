import turtle
import random
import time

window = turtle.Screen()

bok=600 #размер
X=-300 #координати элементив
Y=300
window.setup(bok,bok)
window.bgcolor('black')
window.title('Хрестики нулики')


xo=turtle.Turtle()
xo.color('white')
xo.speed(0)
xo.pensize(7)
xo.hideturtle()

tablica=[[None, None, None],
         [None, None, None],
         [None, None, None]]

cherga=random.choice(['x','o'])

vidstup=int(bok/3)
for i in [1,2]:# малюемо линии
    xo.penup()
    xo.goto(X,Y-i*vidstup)
    xo.pendown()
    xo.goto(-X,Y-i*vidstup)

    xo.penup()
    xo.goto(X+i*vidstup,Y)
    xo.pendown()
    xo.goto(X+i*vidstup,-Y)

def perevirka(): # проверяем кто выиграл
    if tablica[0][0]==tablica[1][1]==tablica[2][2]:return tablica[2][2]
    if tablica[0][2]==tablica[1][1]==tablica[2][0]:return tablica[2][0]

    for ryadok in range(3):
        if tablica[ryadok][0]==tablica[ryadok][1]==tablica[ryadok][2]:return tablica[ryadok][0]
        
    for stovbchik in range(3):
        if tablica[0][stovbchik]==tablica[1][stovbchik]==tablica[2][stovbchik]:return tablica[0][stovbchik]
    return None

def click(x,y): # определяем  какую клетку мы нажимаем
    global cherga
    stovbchik=0
    ryadok=0

    if x<X+vidstup:
        stovbchik=0
    elif x>X+2*vidstup:
        stovbchik=2
    else:
        stovbchik=1

    if y<Y-2*vidstup:
        ryadok=2
    elif y>Y-vidstup:
        ryadok=0
    else:
        ryadok=1

    if tablica[ryadok][stovbchik]!= None: return

    stovbchik_seredinka=(stovbchik*vidstup+vidstup/2)-bok/2 # делаем так, чтоб знак біл в центре клетки
    ryadok_seredinka=(-ryadok*vidstup-vidstup/2)+bok/2

    xo.penup()
    xo.goto(stovbchik_seredinka-20,ryadok_seredinka-20)# ставим в клетку х или о
    if cherga=='x':
        xo.write('x',font=("Arial",50))
    else:
        xo.write('o',font=("Arial",50))
        
    tablica[ryadok][stovbchik]=cherga

    if cherga =='o': cherga='x'
    else: cherga='o'

    if perevirka() !=None: # пишем кто выиграл
        xo.penup()
        xo.goto(-150,0)
        time.sleep(1)
        xo.clear()
        xo.write("WIN"+perevirka(),font=("Arial",100))
    


window.onclick(click)
window.listen()
window.mainloop()

    
