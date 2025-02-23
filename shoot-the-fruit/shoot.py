from random import randint
apple = Actor("apple")
orange = Actor("orange")
pineapple = Actor("pineapple")

fruits = [apple, orange, pineapple]
current_fruit = apple

def draw():
    screen.clear()
    current_fruit.draw()

def place_fruits(current_fruit):
    new_fruit = fruits[randint(0,2)]
    new_fruit.x = randint(10, 800)
    new_fruit.y = randint(10, 600)
    return new_fruit
    
def on_mouse_down(pos):
    if current_fruit.collidepoint(pos):
        print("Good shot!")
        place_fruits(current_fruit)
        current_fruit = place_fruits(current_fruit)
    else:
        print("Game over!")

current_fruit = place_fruits(None)

place_fruits(current_fruit)
