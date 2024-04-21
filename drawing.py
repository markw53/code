from shapes import Paper, Triangle, Rectangle, Oval
paper = Paper()

petal = Oval()
for i in range(0,10):
    petal.randomize()
    petal.draw()

paper.display()
