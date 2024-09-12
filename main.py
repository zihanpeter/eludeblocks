import pgzrun
import time
import random


HEIGHT = 500
WIDTH = 500
TITLE = "Elude Blocks"

ball = Actor("ball.png", [WIDTH / 2, WIDTH / 2])

moveX = 0
moveY = 0
move = 1
timeBegin = time.time()
show = 1
maxShow = int(HEIGHT / 4)
blockList = []
score = 0
end = False
begin = True

for i in range(0, maxShow):
    blockList.append(Actor("ball.png", [WIDTH + 10, random.randint(0, WIDTH)]))

def draw():
    global show, blockList, score, end, begin
    if begin:
        screen.draw.text("Elude Blocks", (40, 200), fontsize = 100, color = "white")
        screen.draw.text("Developed By Peter Lu in 2023.", (120, 275), fontsize = 25, color = "white")
    else:
        screen.fill((0, 0, 0))
        ball.draw()
        cnt = 0
        for i in blockList:
            cnt += 1
            i.draw()
            if cnt == show:
                break
        screen.draw.text("Score: " + str(score), (25, 25), fontsize = 25, color = "white")
        if end:
            screen.draw.text("Game Over", (70, 200), fontsize = 100, color = "white")

def on_key_down(key):
    global moveX, moveY, move
    if key == keys.UP or key == keys.W:
        moveY = -move
    if key == keys.DOWN or key == keys.S:
        moveY = move
    if key == keys.LEFT or key == keys.A:
        moveX = -move
    if key == keys.RIGHT or key == keys.D:
        moveX = move

def on_key_up():
    global moveX, moveY
    moveX = 0
    moveY = 0

def update():
    global moveX, moveY, move, timeBegin, show, maxShow, blockList, score, end, begin
    if not end:
        if ball.x >= move and moveX < 0:
            ball.x += moveX
        if ball.x <= WIDTH - move and moveX > 0:
            ball.x += moveX
        if ball.y >= move and moveY < 0:
            ball.y += moveY
        if ball.y <= HEIGHT - move and moveY > 0:
            ball.y += moveY
    if begin and time.time() - timeBegin >= 3:
        begin = False
    if time.time() - timeBegin >= 15:
        timeBegin = time.time()
        move += 1
        if show < maxShow:
            show += 1
    cnt = 0
    for i in blockList:
        cnt += 1
        if i.x <= 0:
            i.x = WIDTH + 1
            i.y = random.randint(0, WIDTH)
            if not end:
                score += 1
        else:
            i.x -= move / 2
        if cnt == show:
            break
    cnt = 0
    for i in blockList:
        cnt += 1
        if i.colliderect(ball):
            end = True
        if cnt == show:
            break
    
pgzrun.go()
