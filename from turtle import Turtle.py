from turtle import Turtle
bob = Turtle()
def draw_circle(name, r, col, x, y):
    name.penup()
    name.goto(x,y)
    name.pendown()
    name.color(col)
    name.dot(r*2)
draw_circle(bob, 90, "blue", 40, 60)
draw_circle(bob, 60, "white", 60, 40)
draw_circle(bob, 30, "red", 80, 30)

