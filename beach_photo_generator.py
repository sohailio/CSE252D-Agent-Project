# PROMPT: use the python turtle library to redraw this (beach.jpeg) scene. Try and make your representation as accurate as possible

import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Sunset Beach Scene")
screen.setup(width=800, height=600)
turtle.colormode(255)

# Create a turtle for drawing
artist = turtle.Turtle()
artist.speed(0)
artist.hideturtle()

# Helper to draw filled rectangle
def draw_rect(x, y, w, h, color):
    artist.penup(); artist.goto(x, y); artist.pendown()
    artist.color(color); artist.begin_fill()
    for _ in range(2):
        artist.forward(w); artist.right(90)
        artist.forward(h); artist.right(90)
    artist.end_fill()

# 1) Sky gradient (purple → orange → yellow)
def draw_sky():
    top, mid, bot = (138,43,226), (255,140,0), (255,215,0)
    # Purple→Orange
    for i in range(150):
        t = i/149
        color = (
            int(top[0] + (mid[0]-top[0])*t),
            int(top[1] + (mid[1]-top[1])*t),
            int(top[2] + (mid[2]-top[2])*t)
        )
        draw_rect(-400, 300-2*i, 800, 2, color)
    # Orange→Yellow
    for i in range(150):
        t = i/149
        color = (
            int(mid[0] + (bot[0]-mid[0])*t),
            int(mid[1] + (bot[1]-mid[1])*t),
            int(mid[2] + (bot[2]-mid[2])*t)
        )
        draw_rect(-400, 300-300-2*i, 800, 2, color)

# 2) Ocean gradient (deep blue → lighter blue)
def draw_ocean():
    top, bot = (25,25,112), (70,130,180)
    for i in range(100):
        t = i/99
        color = (
            int(top[0] + (bot[0]-top[0])*t),
            int(top[1] + (bot[1]-top[1])*t),
            int(top[2] + (bot[2]-top[2])*t)
        )
        draw_rect(-400, 50-2*i, 800, 2, color)

# 3) Sandy shore
def draw_sand():
    draw_rect(-400, -100, 800, 150, (238,214,175))

# 4) Sun
def draw_sun():
    artist.penup(); artist.goto(0, 50)
    artist.color((255,223,0)); artist.begin_fill()
    artist.circle(40)
    artist.end_fill()

# 5) Random rocks
def draw_rock(x, y, size):
    artist.penup(); artist.goto(x, y); artist.pendown()
    artist.color((80,80,80)); artist.begin_fill()
    for _ in range(6):
        artist.forward(size); artist.right(60)
    artist.end_fill()

# 6) Palm tree (curved trunk + fronds)
def draw_palm(x, y, height, lean):
    # Trunk
    artist.penup(); artist.goto(x, y); artist.pendown()
    artist.color((101,67,33)); artist.pensize(8)
    artist.setheading(90 + lean); artist.forward(height)
    top = artist.position()
    # Fronds
    artist.color((34,139,34)); artist.pensize(3)
    for angle in range(-60, 61, 30):
        artist.penup(); artist.goto(top)
        artist.setheading(90 + lean + angle); artist.pendown()
        artist.forward(60)

# Compose scene
draw_sky()
draw_ocean()
draw_sand()
draw_sun()
for _ in range(5):
    draw_rock(random.randint(-300,100), random.randint(-100,0), random.randint(20,50))
palm_data = [(-150,-100,100,-15), (-100,-100,130,-10), (150,-90,120,10), (180,-110,140,15)]
for x,y,h,ln in palm_data:
    draw_palm(x, y, h, ln)

turtle.done()