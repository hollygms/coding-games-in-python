from random import randint
WIDTH = 400
HEIGHT = 400
fox_speed = 4
score = 0
game_over = False
game_time = 7.0


fox = Actor("fox")
fox.pos = 100, 100

coin = Actor("coin")
coin.pos = 200, 200

def draw():
    screen.fill("green")
    fox.draw()
    coin.draw()
    screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))

    if game_over:
        screen.fill("pink")
        screen.draw.text("Final Score: " + str(score), topleft=(10, 10), fontsize=60)

def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))

def time_up():
    global game_over
    game_over = True

def update():
    global score
    
    if keyboard.left:
        fox.x = fox.x - fox_speed
    elif keyboard.right:
        fox.x = fox.x + fox_speed
    elif keyboard.up:
        fox.y = fox.y - fox_speed
    elif keyboard.down:
        fox.y = fox.y + fox_speed

    coin_collected = fox.colliderect(coin)

    if coin_collected:
        score = score + 10
        place_coin()

clock.schedule(time_up, game_time)
place_coin()
