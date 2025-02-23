from random import randint

WIDTH = 400
HEIGHT = 400

dots = []
lines = []

next_dot = 0
number_of_dots = 3
level = 0


for dot in range(0, number_of_dots):
    actor = Actor("dot")
    actor.pos = randint(20, WIDTH - 20), randint(20, HEIGHT - 20)
    dots.append(actor)


def draw():
    screen.fill("black")
    number = 1
    for dot in dots:
        screen.draw.text(str(number), (dot.pos[0], dot.pos[1] + 12))
        dot.draw()
        number = number + 1
    for line in lines:
        screen.draw.line(line[0], line[1], (100, 0, 0))
        
def redraw(dots, lines, next_dot):
    dots = []
    lines = []
    next_dot = 0
    for dot in range(0, number_of_dots):
        actor = Actor("dot")
        actor.pos = randint(20, WIDTH - 20), randint(20, HEIGHT - 20)
        dots.append(actor)

def new_game(lines, next_dot):
    lines = []
    next_dot = 0
    return lines, next_dot


def next_level():
    global number_of_dots
    new_game(lines, next_dot)
    number_of_dots += 2
    redraw(dots, lines, next_dot)

def on_mouse_down(pos):
    global next_dot
    global lines
    global level
    if next_dot < len(dots) and dots[next_dot].collidepoint(pos):
        if next_dot:
            lines.append((dots[next_dot - 1].pos, dots[next_dot].pos))
        next_dot = next_dot + 1
    elif next_dot == len(dots):
        print("level up")
        next_level()
    else:
        print("redrawing")
        redraw(dots, lines, next_dot)
