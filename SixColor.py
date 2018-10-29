# SixColor.py
import turtle
t = turtle.Pen()
colors = ["red", "yellow", "orange", "pink", "purple", "blue"]
for x in range(100):
    t.pencolor(colors[x%6])
    t.forward(x)
    t.left(60)
