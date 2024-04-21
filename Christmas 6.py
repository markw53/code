from turtle import *

speed(0)
setup(800,700)

#blue background
penup()
goto(0,-320)
pendown()
color("lightskyblue")
begin_fill()
circle(320)
end_fill()

# bottom of body
penup()
goto(0,-280)
pendown()
color("white")
begin_fill()
circle(110)
end_fill()

#middle of body
penup()
goto(0,-110)
pendown()
begin_fill()
circle(90)
end_fill()

#head of snowman
penup()
goto(0,20)
pendown()
begin_fill()
circle(70)
end_fill()

#function to fraw 1 small black circle
def black_circle():
    color("black")
    begin_fill()
    circle(10)
    end_fill()

#eyes
x = -20
for i in range(2):
   penup()
   goto(x,110)
   pendown()
   black_circle()
   x = x + 40

#buttons
y = 0
for i in range(5):
    penup()
    goto(0,y)
    pendown()
    black_circle()
    y = y - 55

#mouth
penup()
goto(0,70)
pendown()
color("red")
begin_fill()
circle(17)
end_fill()

#right arm
penup()
goto(75,0)
pendown()
color("brown")
begin_fill()
left(40)
for i in range(2):
    forward(75)
    left(90)
    forward(7)
    left(90)
end_fill()

#right finger 1
penup()
goto(115,38)
pendown()
begin_fill()
left(40)
for i in range(2):
    forward(25)
    left(90)
    forward(5)
    left(90)
end_fill()

#right finger 2
begin_fill()
right(100)
for i in range(2):
    forward(25)
    left(90)
    forward(5)
    left(90)
end_fill()

#left arm
penup()
goto(-130,50)
pendown()
begin_fill()
right(10)
for i in range(2):
    forward(75)
    right(90)
    forward(7)
    right(90)
end_fill()

#left finger 1
penup()
goto(-112,58)
pendown()
begin_fill()
right(40)
for i in range(2):
    forward(25)
    right(90)
    forward(5)
    right(90)
end_fill()

#left finger 2
begin_fill()
right(100)
penup()
goto(-108,31)
pendown()
for i in range(2):
    forward(25)
    right(90)
    forward(5)
    right(90)
end_fill()

#hat
penup()
goto(50,150)
pendown()
color("black")
begin_fill()
right(10)
forward(100)
right(90)
forward(10)
right(90)
forward(20)
left(90)
forward(45)
right(90)
forward(60)
right(90)
forward(45)
left(90)
forward(20)
right(90)
end_fill()

#text on screen
penup()
goto(-130,230)
pendown()
color("red")
write("HAPPY CHRISTMAS!", font=("Arial", 20, "bold"))

hideturtle()


    
        
