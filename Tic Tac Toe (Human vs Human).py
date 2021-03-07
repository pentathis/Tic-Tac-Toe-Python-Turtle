#Tic Tac Toe Game Using Turtle Module
#By Kaustubh Kulkarni

import turtle as t

#Window
wn = t.Screen()
wn.title("Tic Tac Toe")
wn.bgcolor("#14BDAC")
wn.setup(width=500, height=500)

#Game variable
gamevar = "×"

#Winning variable
play=True

#Cell Variables
grid=[[0,0,0],[0,0,0],[0,0,0]]

#Grid Pen: This turtle gives the title and raws the grid.

#The Title: Tic tac Toe
grid_pen = t.Turtle()
grid_pen.ht()
grid_pen.penup()
grid_pen.speed(0)
grid_pen.goto(0,190)
grid_pen.color("#FFFFFF")
grid_pen.write("Tac ", align="center", font=("Sans serif", 30, "normal"))
grid_pen.color("#545454")
grid_pen.write("Tic        Toe", align="center", font=("Sans serif", 30, "normal"))

#Grid drawing
grid_pen.ht()
grid_pen.color("#0DA192")
grid_pen.pensize(10)
grid_pen.speed(0)
grid_pen.penup()
grid_pen.goto(-55,-220)
grid_pen.pendown()
grid_pen.lt(90)
grid_pen.fd(320)
grid_pen.penup()
grid_pen.goto(55,100)
grid_pen.rt(180)
grid_pen.pendown()
grid_pen.fd(320)
grid_pen.penup()
grid_pen.goto(160,-115)
grid_pen.rt(90)
grid_pen.pendown()
grid_pen.fd(320)
grid_pen.penup()
grid_pen.goto(-160,-5)
grid_pen.rt(180)
grid_pen.pendown()
grid_pen.fd(320)

#Status Turtle
status = t.Turtle()
status.ht()
status.penup()
status.color("#545454")
status.speed(0)
status.goto(-160,131)
status.write(gamevar, align="left", font=("Sans serif", 30, "normal"))
status.goto(-160,140)
status.write("    Turn", align="left", font=("Sans serif", 20, "normal"))

#Reset Turtle
reset = t.Turtle()
reset.ht()
reset.penup()
reset.color("#545454")
reset.speed(0)
reset.goto(160,140)
reset.write("Reset", align="right", font=("Sans serif", 20, "normal"))

#XO Pen
xo_pen = t.Turtle()
xo_pen.ht()
xo_pen.color("#545454")
xo_pen.speed(0)
xo_pen.penup()
    
def rst(x,y):
    global gamevar
    global grid
    global play

    #Winner functions
    
    def x_winner():
        global play
        play=False
        status.clear()
        status.goto(-160,131)
        status.color("#545454")
        status.write("×", align="left", font=("Sans serif", 30, "normal"))
        status.goto(-160,140)
        status.write("    Won!", align="left", font=("Sans serif", 20, "normal"))
       
    def o_winner():
        global play
        play=False
        status.clear()
        status.goto(-160,131)
        status.color("#FFFFFF")
        status.write("○", align="left", font=("Sans serif", 35, "normal"))
        status.goto(-160,140)
        status.write("    Won!", align="left", font=("Sans serif", 20, "normal"))

    def game_draw():
        status.clear()
        status.color("#545454")
        status.goto(-160,140)
        status.write("Draw!", align="left", font=("Sans serif", 20, "normal"))
        
    def draw_xo():
        global gamevar
        if gamevar=="×" and play==True:
            xo_pen.color("#545454")
            xo_pen.penup()
            xo_pen.write(gamevar, align="center", font=("Sans serif", 100, "normal"))
            gamevar="○"
            status.goto(-160,131)
            status.clear()
            status.color("#FFFFFF")
            status.write(gamevar, align="left", font=("Sans serif", 35, "normal"))
            status.goto(-160,140)
            status.write("    Turn", align="left", font=("Sans serif", 20, "normal"))
            #X Winner 
            if grid[0][0]=="×" and grid[0][1]=="×" and grid[0][2]=="×":
                x_winner()
                xo_pen.goto(-160,50)
                xo_pen.color("#545454")
                xo_pen.pensize(10)
                xo_pen.pendown()
                xo_pen.goto(160,50)
                xo_pen.penup()
            if grid[1][0]=="×" and grid[1][1]=="×" and grid[1][2]=="×":
                x_winner()
                xo_pen.goto(-160,-60)
                xo_pen.color("#545454")
                xo_pen.pensize(10)
                xo_pen.pendown()
                xo_pen.goto(160,-60)
                xo_pen.penup()
            if grid[2][0]=="×" and grid[2][1]=="×" and grid[2][2]=="×":
                x_winner()
                xo_pen.goto(-160,-170)
                xo_pen.color("#545454")
                xo_pen.pensize(10)
                xo_pen.pendown()
                xo_pen.goto(160,-170)
                xo_pen.penup()
            if grid[0][0]=="×" and grid[1][0]=="×" and grid[2][0]=="×":
                x_winner()
                xo_pen.goto(-110,100)
                xo_pen.color("#545454")
                xo_pen.pensize(10)
                xo_pen.pendown()
                xo_pen.goto(-110,-220)
                xo_pen.penup()
            if grid[0][1]=="×" and grid[1][1]=="×" and grid[2][1]=="×":
                x_winner()
                xo_pen.goto(0,100)
                xo_pen.color("#545454")
                xo_pen.pensize(10)
                xo_pen.pendown()
                xo_pen.goto(0,-220)
                xo_pen.penup()
            if grid[0][2]=="×" and grid[1][2]=="×" and grid[2][2]=="×":
                x_winner()
                xo_pen.goto(110,100)
                xo_pen.color("#545454")
                xo_pen.pensize(10)
                xo_pen.pendown()
                xo_pen.goto(110,-220)
                xo_pen.penup()
            if grid[0][0]=="×" and grid[1][1]=="×" and grid[2][2]=="×":
                x_winner()
                xo_pen.goto(-160,100)
                xo_pen.color("#545454")
                xo_pen.pensize(10)
                xo_pen.pendown()
                xo_pen.goto(160,-220)
                xo_pen.penup()
            if grid[2][0]=="×" and grid[1][1]=="×" and grid[0][2]=="×":
                x_winner()
                xo_pen.goto(160,100)
                xo_pen.color("#545454")
                xo_pen.pensize(10)
                xo_pen.pendown()
                xo_pen.goto(-160,-220)
                xo_pen.penup()
                
        elif gamevar=="○" and play==True:
            xo_pen.color("#FFFFFF")
            xo_pen.penup()
            xo_pen.write(gamevar, align="center", font=("Sans serif", 110, "bold"))
            gamevar="×"
            status.goto(-160,131)
            status.clear()
            status.color("#545454")
            status.write(gamevar, align="left", font=("Sans serif", 30, "normal"))
            status.goto(-160,140)
            status.write("    Turn", align="left", font=("Sans serif", 20, "normal"))
            #O Winner
            if grid[0][0]=="○" and grid[0][1]=="○" and grid[0][2]=="○":
                o_winner()
                xo_pen.goto(-160,50)
                xo_pen.color("#FFFFFF")
                xo_pen.pensize(10)
                xo_pen.pendown()
                xo_pen.goto(160,50)
                xo_pen.penup()
            if grid[1][0]=="○" and grid[1][1]=="○" and grid[1][2]=="○":
                o_winner()
                xo_pen.goto(-160,-60)
                xo_pen.color("#FFFFFF")
                xo_pen.pensize(10)
                xo_pen.pendown()
                xo_pen.goto(160,-60)
                xo_pen.penup()
            if grid[2][0]=="○" and grid[2][1]=="○" and grid[2][2]=="○":
                o_winner()
                xo_pen.goto(-160,-170)
                xo_pen.color("#FFFFFF")
                xo_pen.pensize(10)
                xo_pen.pendown()
                xo_pen.goto(160,-170)
                xo_pen.penup()
            if grid[0][0]=="○" and grid[1][0]=="○" and grid[2][0]=="○":
                o_winner()
                xo_pen.goto(-110,100)
                xo_pen.color("#FFFFFF")
                xo_pen.pensize(10)
                xo_pen.pendown()
                xo_pen.goto(-110,-220)
                xo_pen.penup()
            if grid[0][1]=="○" and grid[1][1]=="○" and grid[2][1]=="○":
                o_winner()
                x_winner()
                xo_pen.goto(0,100)
                xo_pen.color("#FFFFFF")
                xo_pen.pensize(10)
                xo_pen.pendown()
                xo_pen.goto(0,-220)
            if grid[0][2]=="○" and grid[1][2]=="○" and grid[2][2]=="○":
                o_winner()
                xo_pen.goto(110,100)
                xo_pen.color("#FFFFFF")
                xo_pen.pensize(10)
                xo_pen.pendown()
                xo_pen.goto(110,-220)
                xo_pen.penup()
            if grid[0][0]=="○" and grid[1][1]=="○" and grid[2][2]=="○":
                o_winner()
                xo_pen.goto(-160,100)
                xo_pen.color("#FFFFFF")
                xo_pen.pensize(10)
                xo_pen.pendown()
                xo_pen.goto(160,-220)
                xo_pen.penup()
            if grid[2][0]=="○" and grid[1][1]=="○" and grid[0][2]=="○":
                o_winner()
                xo_pen.goto(160,100)
                xo_pen.color("#FFFFFF")
                xo_pen.pensize(10)
                xo_pen.pendown()
                xo_pen.goto(-160,-220)
                xo_pen.penup()

        if grid[0][0]!=0 and grid[0][1]!=0 and grid[0][2]!=0 and grid[1][0]!=0 and grid[1][1]!=0 and grid[1][2]!=0 and grid[2][0]!=0 and grid[2][1]!=0 and grid[2][2]!=0 and play==True:
            game_draw()

    if x>80 and x<164 and y>140 and y<175:
        xo_pen.clear()
        grid=[[0,0,0],[0,0,0],[0,0,0]]
        gamevar = "×"
        play=True
        status.clear()
        status.color("#545454")
        status.goto(-160,131)
        status.write(gamevar, align="left", font=("Sans serif", 30, "normal"))
        status.goto(-160,140)
        status.write("    Turn", align="left", font=("Sans serif", 20, "normal"))
        
    if x>-160 and x<-60 and y>0 and y<100 and grid[0][0]==0:
        xo_pen.goto(-110,-25)#50
        grid[0][0]=gamevar
        draw_xo()
    if x>-50 and x<50 and y>0 and y<100 and grid[0][1]==0:
        xo_pen.goto(0,-25)
        grid[0][1]=gamevar
        draw_xo()
    if x>60 and x<160 and y>0 and y<100 and grid[0][2]==0:
        xo_pen.goto(110,-25)
        grid[0][2]=gamevar
        draw_xo()
    if x>-160 and x<-60 and y>-110 and y<-10 and grid[1][0]==0:
        xo_pen.goto(-110,-135)
        grid[1][0]=gamevar
        draw_xo()
    if x>-50 and x<50 and y>-110 and y<-10 and grid[1][1]==0:
        xo_pen.goto(0,-135)
        grid[1][1]=gamevar
        draw_xo()
    if x>60 and x<160 and y>-110 and y<-10 and grid[1][2]==0:
        xo_pen.goto(110,-135)
        grid[1][2]=gamevar
        draw_xo()
    if x>-160 and x<-60 and y>-220 and y<-120 and grid[2][0]==0:
        xo_pen.goto(-110,-245)
        grid[2][0]=gamevar
        draw_xo()
    if x>-50 and x<50 and y>-220 and y<-120 and grid[2][1]==0:
        xo_pen.goto(0,-245)
        grid[2][1]=gamevar
        draw_xo()
    if x>60 and x<160 and y>-220 and y<-120 and grid[2][2]==0:
        xo_pen.goto(110,-245)
        grid[2][2]=gamevar
        draw_xo()
         
#Listening to mouse click
t.onscreenclick(rst)
t.listen()
t.done()