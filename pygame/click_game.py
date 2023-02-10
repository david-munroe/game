import time

character = Actor("character_2")
character.pos = 150, 150
WIDTH = 300
HEIGHT = 300
num = 0
speed = 1
count = 0


def draw():
    screen.fill((24, 62, 1))
    character.draw()


def update():
    global count
    character.left = character.left + speed
    count = count + 1
    if count == 150:
        count = 0
        time.sleep(3)
    if character.left > WIDTH:
        character.right = 150

def on_mouse_down(pos):
    global num
    global speed
    if character.collidepoint(pos) and num == 0:
        character.image = "character_2_react"
        num = num + 1
        speed = speed + .9
        sounds.chime.play()
    elif character.collidepoint(pos) and num == 1:
        character.image = "character_2"
        num = num - 1
        speed = 1
