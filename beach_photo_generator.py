# PROMPT: use the python turtle library to redraw this (beach.jpg) scene. Try and make your representation as accurate as possible
import turtle
import colorsys

# ——— Helper functions ———

def lerp(a, b, t):
    """Linear interpolation between a and b."""
    return a + (b - a) * t

def color_lerp(c1, c2, t):
    """Interpolate between two RGB colors (tuples of 0–1 floats)."""
    return (lerp(c1[0], c2[0], t),
            lerp(c1[1], c2[1], t),
            lerp(c1[2], c2[2], t))

def draw_gradient_rect(y1, y2, c1, c2, steps=100):
    """Draw a vertical gradient between y1 and y2."""
    height = y2 - y1
    for i in range(steps):
        t = i / (steps - 1)
        c = color_lerp(c1, c2, t)
        turtle.color(c)
        turtle.penup()
        turtle.goto(-screen_width/2, y1 + t * height)
        turtle.pendown()
        turtle.begin_fill()
        turtle.goto(screen_width/2, y1 + t * height)
        turtle.goto(screen_width/2, y1 + (t + 1/steps) * height)
        turtle.goto(-screen_width/2, y1 + (t + 1/steps) * height)
        turtle.goto(-screen_width/2, y1 + t * height)
        turtle.end_fill()

def draw_sun(x, y, radius, color):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.color(color)
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(radius)
    turtle.end_fill()

def draw_palm_trunk(x, y, height, curve, thickness=5):
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(90 - curve)
    turtle.pensize(thickness)
    turtle.color("black")
    turtle.pendown()
    turtle.forward(height)

def draw_palm_leaf(x, y, heading, length, spread, thickness=2):
    """Draw one leaf as a curved line of small segments."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(heading)
    turtle.pensize(thickness)
    turtle.color("black")
    turtle.pendown()
    for i in range(int(length / 5)):
        turtle.forward(5)
        turtle.right(spread)

def draw_palm(x, y, scale=1.0):
    """Draw a simple palm tree silhouette."""
    h = 100 * scale
    curve = 15 * scale
    draw_palm_trunk(x, y, h, curve, thickness=6*scale)
    # Leaves
    leaf_len = 80 * scale
    for angle in (-60, -30, 0, 30, 60):
        draw_palm_leaf(x, y + h, 90 + angle, leaf_len, -2)

def draw_rock(x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.color("black")
    turtle.begin_fill()
    turtle.pendown()
    # approximate a rounded polygon
    sides = 6
    for _ in range(sides):
        turtle.forward(size)
        turtle.left(360 / sides + 10)
    turtle.end_fill()

# ——— Setup screen ———

screen = turtle.Screen()
screen_width, screen_height = 800, 600
screen.setup(screen_width, screen_height)
screen.title("Sunset Beach — Turtle")

# Use colormode 1.0 for easy interpolation
turtle.colormode(1.0)
turtle.speed(0)
turtle.hideturtle()
turtle.tracer(False)

# ——— Draw sky gradient ———

# Top sky: violet → pink
draw_gradient_rect(screen_height/2, 50,
                   colorsys.hsv_to_rgb(0.75, 0.4, 0.6),
                   colorsys.hsv_to_rgb(0.02, 0.6, 0.95),
                   steps=120)

# Horizon band: pink → orange
draw_gradient_rect(50, 0,
                   colorsys.hsv_to_rgb(0.02, 0.6, 0.95),
                   colorsys.hsv_to_rgb(0.10, 0.8, 0.98),
                   steps=80)

# ——— Draw sun ———

draw_sun(0, 0, 40, colorsys.hsv_to_rgb(0.10, 0.9, 1.0))

# ——— Draw water gradient ———

# Just below horizon down to y = -100
draw_gradient_rect(0, -100,
                   colorsys.hsv_to_rgb(0.10, 0.7, 0.9),
                   colorsys.hsv_to_rgb(0.10, 0.3, 0.6),
                   steps=100)

# ——— Draw sand ———

draw_gradient_rect(-100, -300,
                   colorsys.hsv_to_rgb(0.10, 0.5, 0.8),
                   colorsys.hsv_to_rgb(0.10, 0.6, 0.9),
                   steps=80)

# ——— Draw palms ———

# Cluster on right
for offset, sc in [(-50, 1.2), (0, 1.0), (30, 0.9), (60, 0.7)]:
    draw_palm(200 + offset, -100, scale=sc)

# A single one on the left
draw_palm(-250, -80, scale=0.8)

# ——— Draw rocks on shore ———

for x, y, s in [(-100, -120, 30), (20, -140, 40), (80, -130, 25), (150, -110, 35)]:
    draw_rock(x, y, s)

turtle.update()
turtle.done()