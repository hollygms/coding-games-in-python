from random import randint
apple = Actor("apple")
orange = Actor("orange")
pineapple = Actor("pineapple")

fruits = [apple, orange, pineapple]
current_fruit = apple

def draw():
    screen.clear()
    current_fruit.draw()

def place_fruits():
    current_fruit.x = randint(10, 800)
    current_fruit.y = randint(10, 600)
    pick_new_fruit()


def pick_new_fruit():
    global current_fruit
    current_fruit = fruits[randint(0,2)]
    
    
def on_mouse_down(pos):
    if current_fruit.collidepoint(pos):
        print("Good shot!")
        place_fruits()
    else:
        print("Game over!")

place_fruits()
