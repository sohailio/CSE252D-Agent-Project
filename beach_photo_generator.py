# PROMPT: here is the generated image, please improve it to match the original image that was provided. Please point out what changes you are making and why you are making them
import turtle
import random
import math

# ——— Setup ———
screen = turtle.Screen()
screen.title("Sunset Beach Scene (Improved)")
screen.setup(width=800, height=600)
turtle.colormode(255)
artist = turtle.Turtle()
artist.speed(0)
artist.hideturtle()

# ——— Helpers ———
def draw_rect(x, y, w, h, color):
    artist.penup(); artist.goto(x, y); artist.pendown()
    artist.color(color); artist.begin_fill()
    for _ in range(2):
        artist.forward(w); artist.right(90)
        artist.forward(h); artist.right(90)
    artist.end_fill()

def lerp(color1, color2, t):
    return tuple(int(color1[i] + (color2[i]-color1[i])*t) for i in range(3))

# ——— 1) Sky gradient ———
def draw_sky():
    top, mid, bot = (138,43,226), (255,140,0), (255,215,0)
    # span from y=300 down to y=100
    for i in range(200):
        t = i/199
        if t < 0.5:
            c = lerp(top, mid, t*2)
        else:
            c = lerp(mid, bot, (t-0.5)*2)
        draw_rect(-400, 300- (i*2), 800, 2, c)

# ——— 2) Ocean + horizon ———
def draw_ocean():
    deep, shallow = (20,20,80), (70,130,180)
    for i in range(120):
        t = i/119
        c = lerp(deep, shallow, t)
        draw_rect(-400, 100- i*2, 800, 2, c)
    # thin darker horizon line
    draw_rect(-400, 100, 800, 2, (10,10,50))

# ——— 3) Sand with wet-sand highlight ———
def draw_sand():
    sand = (238,214,175)
    wet = (220,190,150)
    draw_rect(-400, -200, 800, 300, sand)
    # wet sand band
    draw_rect(-400, -80, 800, 40, wet)

# ——— 4) Sun + reflection ———
def draw_sun_and_reflection():
    # sun
    artist.penup(); artist.goto(0, 60); artist.pendown()
    artist.color((255,223,0)); artist.begin_fill(); artist.circle(40); artist.end_fill()
    # reflection: a vertical fading oval
    for i in range(20):
        alpha = 1 - i/19
        col = (int(255*alpha+shallow[0]*(1-alpha)),
               int(223*alpha+shallow[1]*(1-alpha)),
               int(0*alpha + shallow[2]*(1-alpha)))
        draw_rect(-40, 60- i*5, 80, 5, col)

# ——— 5) Irregular rocks ———
def draw_rock(x, y, scale):
    verts = random.randint(5,8)
    angles = [random.uniform(0,360) for _ in range(verts)]
    angles.sort()
    artist.penup(); artist.goto(x + math.cos(math.radians(angles[0]))*scale,
                               y + math.sin(math.radians(angles[0]))*scale)
    artist.pendown(); artist.color((70,70,70)); artist.begin_fill()
    for a in angles[1:]:
        artist.goto(x + math.cos(math.radians(a))*scale*random.uniform(0.8,1.2),
                     y + math.sin(math.radians(a))*scale*random.uniform(0.8,1.2))
    artist.end_fill()

# ——— 6) More natural palms ———
def draw_palm(x, y, height, bend):
    # trunk as two segments to simulate curve
    artist.penup(); artist.goto(x, y); artist.pendown()
    artist.color((101,67,33)); artist.pensize(8)
    artist.setheading(90 + bend/2)
    artist.forward(height*0.6)
    artist.setheading(90 + bend)
    artist.forward(height*0.4)
    top = artist.position()
    # fronds: more, varied lengths
    artist.color((34,139,34)); artist.pensize(2)
    for angle in range(-75, 76, 25):
        length = random.uniform(50,80)
        artist.penup(); artist.goto(top)
        artist.setheading(angle + bend + 90); artist.pendown()
        artist.forward(length)

# ——— Compose improved scene ———
draw_sky()
draw_ocean()
draw_sand()
# capture shallow for reflection blend
shallow = (70,130,180)
draw_sun_and_reflection()

# rocks
for _ in range(7):
    draw_rock(random.randint(-300,150), random.randint(-150,-50), random.randint(15,40))

# palms
palms = [(-160,-180,120,-20), (-80,-170,140,-10), (140,-180,130,10), (180,-190,150,20)]
for x,y,h,b in palms:
    draw_palm(x, y, h, b)

turtle.done()