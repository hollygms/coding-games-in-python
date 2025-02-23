HEIGHT = 800
WIDTH = 600

tree = Actor("tree")
tree.pos = (350, 450)
house = Actor("house")
house.pos = (300, 460)

def draw():
    screen.blit("background", (0,0))
    tree.draw()
    house.draw()

def move_item(item):
    item.x -= 20
    print("moving " + str(item))

def on_mouse_down():
    move_item(house)
    move_item(tree)
    print("is this working?")



