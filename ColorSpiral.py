# ColorSpiral.py
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
# You can choose between 2 and 6 sides for some cool shapes!
sides = eval(input("Enter a number of sides between 2 and 6: "))
tiri = eval(input("Enter a number of range: "))
colors = ["red", "yellow", "blue", "orange", "green", "purple", "pink", "white"]
for x in range(tiri):
    t.pencolor(colors[x%sides])
    t.forward(x * 3/sides + x)
    t.left(360/sides + 1)
    t.width(x*sides/200)
