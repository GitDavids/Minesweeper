import turtle, random, webbrowser
'''This is the actual game'''
#setup and reading in selected settings from a text file created by the previous wind(programm)
turtle.ht()
f=open('setup.txt')
info=f.readline()
Setup=info.split(':::')
DimInput=Setup[0]
Mines=Setup[1]
T=turtle.Turtle()
T.ht()
T.pensize=(5*int(DimInput))
turtle.getscreen()
turtle.colormode(255)
turtle.bgcolor(190,190,190)
screen=turtle.Screen()
screen.setup(width=1.0, height=1.0, startx=None, starty=None)

Row=0
Square=0
mistakes=0
numAdjMines=0
#I'll be using (Row,Square) cordinate system for a grid.
#Rows act like y cordinates and Squares act like x cordinates

#Now I define a few functions, which are labeled#
    
'''Draws a line of squares in the grid'''
def line(DimInput):
    for i in range (72//int(DimInput)):
        T.seth(0)
        for i in range (4):
            T.fd(20*int(DimInput))
            T.rt(90)
        T.fd(20*int(DimInput))
        
'''Counts the number of adjacent mines'''
def adjacentmines(Row, Square, DimInput):
    numAdjMines=0
#Left/Right
    if Square !=(72//int(DimInput)-1) and mines[Row][Square+1] == 1:
        numAdjMines+=1
    if Square != 0 and mines[Row][Square-1] == 1:
        numAdjMines+=1
#Top left/Top right/top
    if Row != (36//int(DimInput))-1 and Square != (72//int(DimInput)-1) and mines[Row+1][Square+1] == 1:
        numAdjMines+=1
    if Row != (36//int(DimInput))-1 and mines[Row+1][Square] == 1:
        numAdjMines+=1
    if Row != (36//int(DimInput))-1 and Square != 0 and mines[Row+1][Square-1] == 1:
        numAdjMines+=1
#Bottom left/Bottom right/Bottom
    if Square != (72//int(DimInput)-1) and Row !=0 and mines[Row-1][Square+1] == 1:
        numAdjMines+=1
    if Row != 0 and mines[Row-1][Square] == 1:
        numAdjMines+=1
    if Row!= 0 and Square != 0 and mines[Row-1][Square-1] == 1:
        numAdjMines+=1
    return numAdjMines

'''From y cordinates returns the row of the square clicked on'''
def R(y):#R for Row
    if y>0:
        R = int(abs(y//(20*int(DimInput))+1 - (36/int(DimInput))/2))
    else:
        R = int(abs(y//(20*int(DimInput)))-1 + (36/int(DimInput))/2)
    return R

'''From x cordinates returns the column the square clicked on is located in'''
def S(x):#S for Square
    if x>0:
        S = int(x//(20*int(DimInput))+36/int(DimInput))
    else:
        S = int(abs(abs(x//(20*int(DimInput)))-36/int(DimInput)))
    return S

'''Reveals one square based on (Row,Square) cordinates'''
def revealONE(Row,Square):
    numAdjMines = adjacentmines(Row, Square, DimInput)#function
    if numAdjMines == 0:
        turtle.tracer(0, 0)
        T.pu()
        T.goto(-720+(Square*int(DimInput)*20),360-(Row*int(DimInput)*20))
        T.seth(0)
        T.pd()
        T.fillcolor(255,255,255)
        T.begin_fill()
        for i in range (4):
            T.fd(20*int(DimInput))
            T.rt(90)
        T.end_fill()
        T.pd()
        turtle.update()
    else:
        turtle.tracer(0, 0)
        T.pu()
        T.goto(-720+(Square*int(DimInput)*20)+(10*int(DimInput)),360-(Row*int(DimInput)*20)-(10*int(DimInput))-6)
        T.pd()
        T.write(numAdjMines, move=False, align="center", font=("Arial", 10, "normal"))
        turtle.update()
    
'''Revelas the sdjacent square info'''
def revealAllAround(Row,Square):
    if Row != 36//int(DimInput)-1:
        if Square != 0:
            revealONE(Row+1,Square-1)
        revealONE(Row+1,Square)
        if Square != 72//int(DimInput)-1:
            revealONE(Row+1,Square+1)
    if Square != 0:
        revealONE(Row,Square-1)
    if Square != 72//int(DimInput)-1:
        revealONE(Row,Square+1)
    if Row != 0:
        if Square != 0:
            revealONE(Row-1,Square-1)
        revealONE(Row-1,Square)
        if Square != 72//int(DimInput)-1:
            revealONE(Row-1,Square+1)

    
'''Reveals the square clicked on (other functions are incorperated in this function)'''
def leftclick(x,y):
    global mistakes
    if -210<x<-160 and 370<y<420:
        Reset()
    if 300<x<400 and 370<y<420:
        url = "info.html"
        webbrowser.open(url)
    elif -720<x<720 and -360<y<360:#Allows to click outside the grid without creating errors 
        Row=R(y)#function
        Square=S(x)#function
        if mines[Row][Square] == 0:
            numAdjMines = adjacentmines(Row, Square, DimInput)#function
            if numAdjMines == 0:
                revealONE(Row,Square)#function
                revealAllAround(Row,Square)#function
            else:
                revealONE(Row,Square)#function
                
        elif mines[Row][Square] == 1:
            mistakes+=1
            turtle.tracer(0,0)
            T.pu()
            T.goto(-630,400)
            T.seth(0)
            T.fillcolor(190,190,190)
            T.begin_fill()
            for i in range (2):
                T.fd(60)
                T.rt(90)
                T.fd(40)
                T.rt(90)
            T.end_fill()
            T.goto(-600,380)
            T.pencolor(255,0,0)
            T.write(mistakes, move=False, align="center", font=("Arial", 16, "normal"))
            T.pencolor(0,0,0)
            T.goto(-720+(Square*int(DimInput)*20)+(10*int(DimInput)),360-(Row*int(DimInput)*20)-(10*int(DimInput))-6)
            T.pd()
            T.pencolor(255,0,0)
            T.write("X", move=False, align="center", font=("Arial", 10, "normal"))
            T.pencolor(0,0,0)
            turtle.update()    

'''Colours the square black if there is a mine if there isn't one a mistake is added'''
def rightclick(x,y):#Colours the square black if there is a mine, if there isn't one a mistake is added########################
    global n,mistakes
    if -720<x<720 and -360<y<360:#Allows to click outside the grid without creating errors 
        Row=R(y)#function
        Square=S(x)#function
        #If on the square there is a mine it is revealed
        if mines[Row][Square]==1:
            turtle.tracer(0, 0)
            T.pu()
            T.goto(-720+(Square*int(DimInput)*20),360-(Row*int(DimInput)*20))
            T.seth(0)
            T.pd()
            T.fillcolor(0,0,0)
            T.begin_fill()
            for i in range (4):
                T.fd(20*int(DimInput))
                T.rt(90)
            T.end_fill()
            T.pd()
            turtle.update()
            n-=1
            T.pu()
            T.goto(-50,400)
            T.seth(0)
            T.fillcolor(190,190,190)
            T.begin_fill()
            for i in range (2):
                T.fd(80)
                T.rt(90)
                T.fd(40)
                T.rt(90)
            T.end_fill()
            T.goto(-10,380)
            T.write(int(n), move=False, align="center", font=("Arial", 16, "normal"))

            if n == 0:
                T.goto(0,0)
                T.pencolor(0,255,0)
                T.write("You won!!!", move=False, align="center", font=("Autumn", 120, "normal"))
            T.pd()
        #If there is not a mine then nothing is regarding to the game play is done and a mistake is added
        #The user can make as many mistakes as he/she wants
        elif mines[Row][Square]==0:
            mistakes+=1
            turtle.tracer(0,0)
            T.pu()
            T.goto(-630,400)
            T.seth(0)
            T.fillcolor(190,190,190)
            T.begin_fill()
            for i in range (2):
                T.fd(60)
                T.rt(90)
                T.fd(40)
                T.rt(90)
            T.end_fill()
            T.goto(-600,380)
            T.pencolor(255,0,0)
            T.write(mistakes, move=False, align="center", font=("Arial", 16, "normal"))
            T.pencolor(0,0,0)
            T.pd()
'''When used for the first time draws the screen but It is also called when the game is reset'''
def Reset():
    global mistakes,N,k,mines,Mines,DimInput,n
    mistakes=0
    screen.reset()
    T.ht()
    turtle.ht()
    #I create a list of lists nth list is the nth row, list called 'mines'
        #Mines with capital M is the proportion of mines
    #nth number in the lists represents the nth square in the row
    #0 = no mine, 1 = square is mined. For now no squares are mined
    mines = []
    k=0
    for i in range (36//int(DimInput)):
        mines.append([])
        for i in range (72//int(DimInput)):
            mines[k].append(0)
        k+=1

    # n = number of mines
    # Mines = mine proportion to squares
    # //1 rounds the number of mines to an integer
    n=0
    if DimInput == "1":
        n=(2592*float(Mines))//1
    elif DimInput == "2":
        n=(648*float(Mines))//1
    elif DimInput == "3":
        n=(288*float(Mines))//1
        
    #N = unique squares with mines
    # n unmined squares are mined
    N=0
    while N != n:
        row = random.randint(0,36//int(DimInput)-1)
        square = random.randint(0,72//int(DimInput)-1)
        if mines[row][square] == 0:
            mines[row][square] = 1
            N+=1

    #Mistake and the number of mines left on the grid counter
    turtle.tracer(0, 0)
    T.pu()
    T.goto(-140,380)
    T.write("There are", move=False, align="left", font=("Arial", 16, "normal"))
    T.goto(-10,380)
    T.write(int(n), move=False, align="center", font=("Arial", 16, "normal"))
    T.goto(30,380)
    T.write("mines left on the grid", move=False, align="left", font=("Arial", 16, "normal"))
    T.goto(-720,380)
    T.write("Mistakes:", move=False, align="left", font=("Arial", 16, "normal"))
    T.goto(-600,380)
    T.write("0", move=False, align="left", font=("Arial", 16, "normal"))
    T.pd()
    y=360

    #Reset button
    turtle.tracer(0,0)
    T.pu()
    T.goto(-210,420)
    T.pd()
    T.fillcolor(255,230,0)
    T.begin_fill()
    for i in range (4):
        T.fd(50)
        T.rt(90)
    T.end_fill()
    T.pu()
    T.goto(-185,385)
    T.pencolor(140,90,0)
    T.write("Reset", move=False, align="center", font=("Arial", 13, "bold"))
    T.pencolor(0,0,0)
    T.pd()
    turtle.update()

    #Draws the grid of quares
    for i in range (36//int(DimInput)):
        T.penup()
        T.goto(-720,y)
        T.pendown()
        y-=20*int(DimInput)
        line(DimInput) 
    turtle.update()

    T.pu()
    T.goto(300,420)
    T.pd()
    T.seth(0)
    T.fillcolor(255,230,0)
    T.begin_fill()
    for i in range (2):
        T.fd(100)
        T.rt(90)
        T.fd(50)
        T.rt(90)
    T.end_fill()
    T.pu() 
    T.goto(350,385)
    T.pd()
    T.pencolor(140,90,0)
    T.write("Info", move=False, align="center", font=("Arial", 13, "bold"))
    T.pencolor(0,0,0)
    
    T.ht()
    turtle.ht()



Reset()

#The 2 left/right click functions
#I wanted to add the middle mouse button but decided not to, because I didn't want users using touch pads to have any problems
turtle.onscreenclick(leftclick,btn=1,add=False)
turtle.onscreenclick(rightclick,3)

turtle.mainloop()

