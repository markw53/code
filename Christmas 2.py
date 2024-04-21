from turtle import*

speed(0)

#blue background
penup()
goto(0,-250)
pendown()
color("lightskyblue")
begin_fill()
circle(250)
end_fill()

#tree trunk
penup()
goto(-15,-50)
pendown()
color("brown")
begin_fill()
for i in range(2):
    forward(30)
    right(90)
    forward(40)
    right(90)
end_fill()

# set the start position and initial tree width
y = -50
width = 240
height = 25

#green section of tree
while width > 20:
    width = width - 30 #make the tree smaller as it goes up
    x = 0-width/2 #set starting x-value of each tree level
    color("green")
    penup()
    goto(x,y)
    pendown()
    begin_fill()
    for i in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()

    y = y + height # keep drawing tree levels higher than previous

#star
penup()
goto(-15,150)
pendown()
color("yellow")
begin_fill()
for i in range(5):
    forward(30)
    right(144)
end_fill()

#message
penup()
goto(-130,-150)
color("red")
write("MERRY CHRISTMAS", font=("Arial", 20, "bold"))

hideturtle()

