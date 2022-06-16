#Tic Tac Toe Game Using Turtle Module Human vs AI (easy)
#By Kaustubh Kulkarni

import turtle as t
from random import choice

#Window
wn = t.Screen()
wn.title("Tic Tac Toe")
wn.bgcolor("#14BDAC")
wn.setup(width=500, height=500)

#Winning variable
play=True

# grid lists  lists
grid_list = ["00","01", "02", "10", "11", "12", "20", "21", "22"]

#Dictionary
dictionary = {"00":(-110,-25), "01":(0,-25), "02":(110, -25),
            "10":(-110,-135), "11":(0,-135), "12":(110, -135),
            "20":(-110,-245), "21":(0,-245), "22":(110, -245),
        }

#Cell Variables
grid=[[0,0,0],[0,0,0],[0,0,0]]

#Grid Pen: This turtle gives the title and draws the grid.

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
xo_pen.penup()
xo_pen.speed(0)

# Click function
def clk(x, y):
    global grid
    global play
    global grid_list

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

    def AI_writes():
        # AI writes o
        try :
            cell = choice(grid_list)

            grid[int(cell[0])][int(cell[1])] = "○"
            xo_pen.color("#FFFFFF")
            xo_pen.goto(dictionary[cell])
            xo_pen.write("○", align="center", font=("Sans serif", 110, "bold"))
            grid_list.remove(cell)
        except IndexError or ValueError:
            pass

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


    #draw xo function
    def draw_xo():

        if play:
            # Write x
            xo_pen.color("#545454")
            xo_pen.write("×", align="center", font=("Sans serif", 100, "normal"))

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

            if grid[0][0]!=0 and grid[0][1]!=0 and grid[0][2]!=0 and grid[1][0]!=0 and grid[1][1]!=0 and grid[1][2]!=0 and grid[2][0]!=0 and grid[2][1]!=0 and grid[2][2]!=0 and play==True:
                game_draw()

            if play:
                AI_writes()
                
    # Reset 
    if x>80 and x<164 and y>140 and y<175:
        xo_pen.clear()
        grid=[[0,0,0],[0,0,0],[0,0,0]]
        grid_list = ["00","01", "02", "10", "11", "12", "20", "21", "22"]
        play=True
        status.clear()
        status.color("#545454")

    # Drawing x on click
    try:
        if x>-160 and x<-60 and y>0 and y<100 and grid[0][0]==0:
            xo_pen.goto(-110,-25)#50
            grid[0][0]="×"
            grid_list.remove("00")
            draw_xo()
        if x>-50 and x<50 and y>0 and y<100 and grid[0][1]==0:
            xo_pen.goto(0,-25)
            grid[0][1]="×"
            grid_list.remove("01")
            draw_xo()
        if x>60 and x<160 and y>0 and y<100 and grid[0][2]==0:
            xo_pen.goto(110,-25)
            grid[0][2]="×"
            grid_list.remove("02")
            draw_xo()
        if x>-160 and x<-60 and y>-110 and y<-10 and grid[1][0]==0:
            xo_pen.goto(-110,-135)
            grid[1][0]="×"
            grid_list.remove("10")
            draw_xo()
        if x>-50 and x<50 and y>-110 and y<-10 and grid[1][1]==0:
            xo_pen.goto(0,-135)
            grid[1][1]="×"
            grid_list.remove("11")
            draw_xo()
        if x>60 and x<160 and y>-110 and y<-10 and grid[1][2]==0:
            xo_pen.goto(110,-135)
            grid[1][2]="×"
            grid_list.remove("12")
            draw_xo()
        if x>-160 and x<-60 and y>-220 and y<-120 and grid[2][0]==0:
            xo_pen.goto(-110,-245)
            grid[2][0]="×"
            grid_list.remove("20")
            draw_xo()
        if x>-50 and x<50 and y>-220 and y<-120 and grid[2][1]==0:
            xo_pen.goto(0,-245)
            grid[2][1]="×"
            grid_list.remove("21")
            draw_xo()
        if x>60 and x<160 and y>-220 and y<-120 and grid[2][2]==0:
            xo_pen.goto(110,-245)
            grid[2][2]="×"
            grid_list.remove("22")
            draw_xo()
    except ValueError:
        pass

#Listening to mouse click
t.onscreenclick(clk)
t.listen()
t.done()