from turtle import *
speed(0)

#background
penup()
goto(0,-300)
pendown()
color("green")
begin_fill()
circle(300)
end_fill()

#red part of hat
penup()
goto(-120,-60)
pendown()
color("red")
begin_fill()
for i in range(3):
    forward(250)
    left(120)
end_fill()

#pom pom
penup()
goto(5,140)
pendown()
color("white")
begin_fill()
circle(20)
end_fill()

#trim on hat
penup()
goto(-105,-80)
pendown()
begin_fill()
for i in range(12):
    circle(20)
    penup()
    forward(20)
    pendown()
end_fill()

#message
penup()
goto(-150,-200)
pendown()
write("HAPPY CHRISTMAS!", font=("Arial", 25, "bold"))

hideturtle()
