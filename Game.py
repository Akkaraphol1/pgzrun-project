import pgzrun
from random import randint

def draw():
    global stgame
    if stgame == 0:
        screen.blit('bggame',(0,0))
        sounds.intro.play()
    elif stgame == 1:
        screen.blit('bggame1',(0,0))
        sounds.intro.stop()
        sounds.music.play()
        screen.draw.text("Score : "+str(score),color='black',topleft=(10,10))
        screen.draw.text("Time : "+str(time),color='black',topleft=(900,10))
        po1.draw()
        po2.draw()
        po3.draw()
        po4.draw()
        po5.draw()
        momo.draw()
        boss.draw()
        boss1.draw()
        boss2.draw()
        if time == maxtime:
            stgame = 4
    elif stgame == 2:
        screen.blit('bggame6',(0,0))
        sounds.music.stop()
        sounds.dead.play()
        screen.draw.text('   Your Score ' +str(score),topleft=(350,350),fontsize=60,color='black')
    elif stgame == 3:
        screen.blit('bggame3',(0,0))
    elif stgame == 4:
        sounds.music.stop()
        if score >= 100:
            screen.draw.text("!!!You Win!!!!",center=(WIDTH/2,HEIGHT/2),fontsize=60,color='black')
            screen.draw.text('   Your Score ' +str(score),topleft=(350,350),fontsize=60,color='black')
        else:
            screen.draw.text("Time out",center=(WIDTH/2,HEIGHT/2),fontsize=60,color='black')
            screen.draw.text('   Your Score ' +str(score),topleft=(350,350),fontsize=60,color='black')        

def on_key_down(key):
    global stgame
    if stgame == 0:
        if key == keys.RETURN:
            start()
            stgame = 1
        if key == keys.SPACE:
            stgame = 3
    if stgame == 2:
        if key == keys.RETURN:
            stgame=0
    if stgame == 3:
        if key == keys.BACKSPACE:
            stgame = 0
    if stgame == 4:
        if key == keys.RETURN:
            stgame=0
    if stgame == 5:
        if key == keys.RETURN:
            stgame=0
    

def update():
    global score,stgame
    if stgame == 1:
        po1.y += 6
        if po1.top > HEIGHT:
            place_po1()
        po2.y += 4
        if po2.top > HEIGHT:
            place_po2()
        po3.y += 5
        if po3.top > HEIGHT:
            place_po3()
        po4.y += 7 
        if po4.top > HEIGHT:
            place_po4()
        po5.y += 9
        if po5.top > HEIGHT:
            place_po5()
        if boss.top > HEIGHT:
            place_boss()
        boss.y += 10
        if boss1.top > HEIGHT:
            place_boss1()
        boss1.y += 11
        if boss2.top > HEIGHT:
            place_boss2()
        boss2.y += 12
        if keyboard.left:
            momo.x -= 3
            if keyboard.up:
                momo.x -= 4
        if keyboard.right:
            momo.x += 3
            if keyboard.up:
                momo.x += 4
        if momo.left == 0:
            momo.left = 0
        if momo.right > WIDTH:
            momo.right = WIDTH
        #คิดคะแนน            
        if momo.colliderect(po1):
            place_po1()
            sounds.eff.play()
            score+=2
        if momo.colliderect(po2):
            place_po2()
            sounds.eff.play()
            score+=1
        if momo.colliderect(po3):
            place_po3()
            sounds.eff.play()
            score+=1
        if momo.colliderect(po4):
            place_po4()
            sounds.eff.play()
            score+=1
        if momo.colliderect(po5):
            place_po5()
            sounds.eff.play()
            score+=1
        if momo.colliderect(boss):
            stgame = 2
        if momo.colliderect(boss1):
            stgame = 2
        if momo.colliderect(boss2):
            stgame = 2
        
def time_count():
    global time
    time += 1
    
def start():
    global stgame,score,time
    time = 0
    score = 0
    stgame = 1
    place_po1()
    place_po2()
    place_po3()
    place_po4()
    place_po5()
    place_boss()
    place_boss1()
    place_boss2()
    
def place_po1():
    for n in range(num):
        x1 = randint (1,WIDTH)
        po1.pos = (x1,0)

def place_po2():
    for n in range(num):
        x2 = randint (1,WIDTH)
        po2.pos = (x2,0)

def place_po3():
    for n in range(num):
        x3 = randint (1,WIDTH)
        po3.pos = (x3,0)

def place_po4():
    for n in range(num):
        x4 = randint (1,WIDTH)
        po4.pos = (x4,0)

def place_po5():
    for n in range(num):
        x5 = randint (1,WIDTH)
        po5.pos = (x5,0)

def place_boss():
    for n in range(num):
        x6 = randint (1,WIDTH)
        boss.pos = (x6,0)

def place_boss1():
    for n in range(num):
        x7 = randint (1,WIDTH)
        boss1.pos = (x7,0)

def place_boss2():
    for n in range(num):
        x8 = randint (1,WIDTH)
        boss2.pos = (x8,0)




#main program
num = 1
score = 0
WIDTH = 1024
HEIGHT = 600
stgame = 0
time = 0
maxtime = 60
momo=(Actor('momo'))
momo.pos=(600,520)

po1=(Actor('po1'))
po2=(Actor('po2'))
po3=(Actor('po3'))
po4=(Actor('po4'))
po5=(Actor('po5'))
boss=(Actor('boss'))
boss1=(Actor('boss1'))
boss2=(Actor('boss2'))

clock.schedule_interval(time_count,1)

pgzrun.go()
        
