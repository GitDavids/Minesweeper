import turtle, random
SetupFile = open("setup.txt","w")

turtle.getscreen()
turtle.ht()
turtle.colormode(255)
turtle.bgcolor(190,190,190)
screen=turtle.Screen()
screen.setup(width=1.0, height=1.0, startx=None, starty=None)

#I create a new turtle and name it "T"
#Initialy I liked calling turtle Thomass but T is shorter
#I do it because it makes the code faster to write/edit
T=turtle.Turtle()
T.ht()

#Writing the titles on the start screen
T.pu()
T.goto(0,200)
T.write('Minesweeper', move=False, align='center', font=("Comic Sans MS", 50, "bold"))
T.goto(0,70)
T.write('Chose grid size', move=False, align='center', font=("Arial", 12, "bold"))
T.goto(0,-160)
T.write('Chose the proportion of mines to grid squares', move=False, align="center", font=("Arial", 12, "bold"))
T.pd()

'''Selection screen left click'''
def select(x, y):
    global DimInput, Mines
    #Dimmension button sensing
    if x>-200 and x<-100 and y<30 and y>-10:
        DimInput=1
    elif x>-50 and x<50 and y<30 and y>-10:
        DimInput=2
    elif x>100 and x<200 and y<30 and y>-10:
        DimInput=3
    if DimInput==1 or DimInput==2 or DimInput==3:

    #Grid dimension illustration, top right corner
        T.pu()
        T.goto(500,320)
        T.fillcolor(190,190,190)
        T.begin_fill()
        for i in range (2):
            T.fd(300)
            T.rt(90)
            T.fd(40)
            T.rt(90)
        T.end_fill()
        T.goto(510,300)
        T.write('Grid size', move=False, align="left", font=("Arial", 12, "bold"))
        T.goto(660,300)
        T.write(Dimensions[DimInput-1], move=False, align="center", font=("Arial", 12, "normal"))
        T.pd()
    #Mine proportion button snesing
    if -520<x<-440 and -200>y>-240:
        Mines=ProportionOfMines[0]
    elif-400<x<-320 and -200>y>-240:
        Mines=ProportionOfMines[1]   
    elif -280< x<-200 and -200>y>-240:
        Mines=ProportionOfMines[2]
    elif -160<x<-80 and -200>y>-240:
        Mines=ProportionOfMines[3]
    elif -40<x<40 and -200>y>-240:
        Mines=ProportionOfMines[4]
    elif 80<x<160 and -200>y>-240:
        Mines=ProportionOfMines[5]
    elif 200<x<280 and -200>y>-240:
        Mines=ProportionOfMines[6]
    elif 320<x<400 and -200>y>-240:
        Mines=ProportionOfMines[7]
    elif 440<x<520 and -200>y>-240:
        Mines=ProportionOfMines[8]

    #Mine proportion illustration, top right corner
    T.pu()
    T.goto(500,270)
    T.fillcolor(190,190,190)
    T.begin_fill()
    for i in range (2):
        T.fd(300)
        T.rt(90)
        T.fd(40)
        T.rt(90)
    T.end_fill()
    T.goto(510,250)
    T.write('Proportion', move=False, align='left', font=('Arial', 12, 'bold'))
    T.goto(660,250)
    T.write(Mines, move=False, align='center', font=('Arial', 12, 'normal'))
    T.pd()
    #Start button sensing, if pressed 'Start Menu.py' file is closed and the actual game is opened
    if -100<x<100 and 100<y<180:
        T.ht()############
        turtle.ht()###########
        SetupFile.write(str(DimInput))
        SetupFile.write(':::')
        SetupFile.write(str(Mines))
        SetupFile.close()
        turtle.resetscreen()
        import Minesweeper_Game
        exec(open('Minesweeper_Game.py').read())
        turtle.bye()
        turtle.ht()
        
        
############################################################################################33
#lists of possible dimensions and mine proportions, and default settings below        
Dimensions = ["72x36","36x18","24x12"]
ProportionOfMines=['0.00','0.05','0.10','0.15','0.20','0.25','0.30','0.35','0.40']
Mines=0.20
DimInput=3

turtle.tracer(0,0)


#Default grid size and proportion of mines      Mines=0.20     DimInput=2
T.pu()
T.goto(510,250)
T.write('Proportion', move=False, align='left', font=('Arial', 12, 'bold'))
T.goto(660,250)
T.write(float(ProportionOfMines[4]), move=False, align="center", font=('Arial', 12, 'normal'))
T.goto(510,300)
T.write('Grid size', move=False, align='left', font=('Arial', 12, 'bold'))
T.goto(660,300)
T.write(Dimensions[DimInput-1], move=False, align="center", font=('Arial', 12, 'normal'))
T.goto(0,100)

#Start button text
T.write('Start', move=False, align='center', font=('Arial', 50, 'bold'))
T.goto(0,180)
T.pd()
#Start button shape
for i in range (2):
    T.fd(100)
    T.rt(90)
    T.fd(80)
    T.rt(90)
    T.fd(100)

#Dimmension input buttons
x=-200
for i in range (3):
    T.pu()
    T.goto(x,30)
    T.pd()
    for v in range (2):
        T.fd(100)
        T.rt(90)
        T.fd(40)
        T.rt(90)
    T.pu()
    T.goto(x+50,0)
    T.pd()
    T.write(Dimensions[i], move=False, align="center", font=("Arial", 14, "normal"))
    x+=150
x=-520
#Mine proportion buttons
R=254
G=254
B=254
for i in range(9):
    T.pu()
    T.goto(x,-200)
    T.pd()
    T.fillcolor(R,G,B)
    T.begin_fill()
    for v in range (2):
        T.fd(80)
        T.rt(90)
        T.fd(40)
        T.rt(90)
    T.end_fill()
    #Colouring in the buttons to resemble some sense of difficulty(white=coimical -> green=easy and sensible -> red-way too many mines)
    if R==254 and G==254 and B==254:
        R-=127
        B-=127
    elif R==127 and G==254 and B==127:
        R-=127
        B-=127
    elif R==0 and G==254 and B==0:
        R+=127
    elif R==127 and G==254 and B==0:
        R+=127
    elif R==254 and G==254 and B==0:
        G-=127
    elif R==254 and G==127 and B==0:
        G-=127
    elif R>0 and G==0 and B==0:
        R-=50
    T.pu()
    T.goto(x+40,-230)
    T.pd()
    T.write(ProportionOfMines[i], move=False, align="center", font=("Arial", 14, "normal"))
    x+=120
    
turtle.update()

turtle.onscreenclick(select,1)

turtle.mainloop()#This keeps the start menu open 
