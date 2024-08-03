import turtle
import random

def langton():
    window = turtle.Screen()
    window.bgcolor('white')
    window.setup(width=1.0, height=1.0)  # Full screen
    window.screensize(1000, 1000)

    maps = {}
    ants = []
    colors = ['red', 'blue', 'green', 'orange', 'purple', 'yellow']

    # Create multiple ants at random locations with random colors
    for _ in range(6):  # Number of ants
        ant = turtle.Turtle()
        ant.shape('square')
        ant.shapesize(0.5)
        ant.speed("fastest")
        ant.penup()
        ant.goto(random.randint(-500, 500), random.randint(-500, 500))  # Random start position
        ant.color(random.choice(colors))
        ants.append(ant)

    while True:
        step = 10
        for ant in ants:
            pos = coordinate(ant)
            if pos not in maps or maps[pos] == "white":
                ant.fillcolor("black")
                ant.stamp()
                invert(maps, ant, "black")
                ant.right(90)
                ant.forward(step)
            elif maps[pos] == "black":
                ant.fillcolor("white")
                invert(maps, ant, "white")
                ant.stamp()
                ant.left(90)
                ant.forward(step)

def invert(graph, ant, color):
    graph[coordinate(ant)] = color

def coordinate(ant):
    return (round(ant.xcor()), round(ant.ycor()))

langton()
