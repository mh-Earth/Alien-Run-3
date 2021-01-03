# __________________________________________importing all modules_________________________________
import pygame 
import math
import random
import time
# __________________________________________________init()_________________________________________
pygame.init()
pygame.mixer.init()
# ______________________________________makeing game display and set title_________________________
display=pygame.display.set_mode((630,950))
pygame.display.set_caption("Alien Run 3")
# ________________________________________all default variable valuse______________________________
running=True
fire=False
remove_bullets=1
score=0
bullets=5
vision_ON=False
vision_TimeOut=200
spaec_ship_position_x=250
spaec_ship_position_y=800
# ____________Positions for astoroides________________
rock1_x=random.randint(10,630)
rock1_y=-500
rock2_x=random.randint(10,630)
rock2_y=0
rock3_x=random.randint(10,630)
rock3_y=-500
rock4_x=random.randint(10,630)
rock4_y=0
# _________________________________________________________
plusbullets_x=random.randint(20,900)
plusbullets_y=random.randint(-5000,-1000)
vision_x=20
vision_y=-random.randint(-6000,-3000)

bullet_y=spaec_ship_position_y
bullet_x=spaec_ship_position_x+45
spaec_ship_v=0
# _______________________________________________________________________________________________________
# _____________________________________________Loading all image_________________________________________
startup=pygame.image.load("startup.jpg")

bg=pygame.image.load("bg.png")
bg=(pygame.transform.scale(bg,(630,950)))
bg2=pygame.image.load("bg.png")
bg2=(pygame.transform.scale(bg2,(630,950)))


rock1=pygame.image.load("rock1.png")
rock1=(pygame.transform.scale(rock1,(100,100)))

rock2=pygame.image.load("rock2.png")
rock2=(pygame.transform.scale(rock2,(200,200)))

rock3=pygame.image.load("rock3.png")
rock3=(pygame.transform.scale(rock3,(100,100)))

rock4=pygame.image.load("rock4.png")
rock4=(pygame.transform.scale(rock4,(100,100)))

spaceShip=pygame.image.load("spaceship.png")
spaceShip=(pygame.transform.scale(spaceShip,(100,100)))

plusbullets=pygame.image.load("plusbullets.png")
plusbullets=(pygame.transform.scale(plusbullets,(50,50)))

vision=pygame.image.load("vision.png")
vision=(pygame.transform.scale(vision,(50,50)))

bullet=pygame.image.load("bullet.png")
bullet=(pygame.transform.scale(bullet,(10,50)))
# ______________________________________________________________________________________________________
# _________________________________________________display clock________________________________________
clock=pygame.time.Clock()
# ______________________________________________________________________________________________________
# ________________________________________function for background moveing_______________________________
bg_y=0
bg2_y=-950
def background():
    global bg_y
    global bg2_y
    display.blit(bg,(0,bg_y))
    display.blit(bg2,(0,bg2_y))
    bg_y+=1
    bg2_y+=1
    if bg_y>950:
        bg_y=-950
    elif bg2_y>950:
        bg2_y=-950
# _______________________________________________________________________________________________________
def calculateDistance(x1,y1,x2,y2):
    global dist
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    # print(dist)
    return dist
# ________________________________________collindig logic for gameover____________________________________
def colliding ():
    global bullets,plusbullets_y,plusbullets_x,vision_ON,vision_x,vision_y
    if calculateDistance(rock1_x,rock1_y,spaec_ship_position_x,spaec_ship_position_y)<100:
        gameover()
    if calculateDistance(rock2_x+100,rock2_y,spaec_ship_position_x+50,spaec_ship_position_y)<150:
        gameover()
    if calculateDistance(rock3_x,rock3_y,spaec_ship_position_x,spaec_ship_position_y)<100:
        gameover()
    if calculateDistance(rock4_x,rock4_y,spaec_ship_position_x,spaec_ship_position_y)<100:
        gameover()
    if calculateDistance(plusbullets_x+15,plusbullets_y+15,spaec_ship_position_x+50,spaec_ship_position_y+50)<80:
        bullets+=5
        plusbullets_x=random.randint(10,600)
        plusbullets_y=-1000
    if calculateDistance(vision_x+15,vision_y+15,spaec_ship_position_x+50,spaec_ship_position_y+50)<80:
        vision_ON=True
        vision_x=random.randint(10,600)
        vision_y=random.randint(-6000,-3000)

# ________________________________________collindig logic for gameover______________________________________
def bulletCollision():
    global rock1_x,rock1_y,rock2_x,rock2_y,rock3_x,rock3_y,rock4_x,rock4_y,fire ,bullet_y,score
    if calculateDistance(rock1_x+50,rock1_y,bullet_x+25,bullet_y)<100:
        score+=1
        rock1_x=random.randint(10,600)
        rock1_y=random.randint(-40,-20)
        fire=False
        bullet_y=spaec_ship_position_y

    if calculateDistance(rock2_x+100,rock2_y+50,bullet_x+25,bullet_y)<100:
        score+=1
        fire=False
        rock2_x=random.randint(10,670)
        rock2_y=random.randint(-300,-200)
        bullet_y=spaec_ship_position_y

    if calculateDistance(rock3_x+50,rock3_y,bullet_x+25,bullet_y)<100:
        score+=1
        fire=False
        rock3_x=random.randint(10,670)
        rock3_y=-40
        bullet_y=spaec_ship_position_y

    if calculateDistance(rock4_x+50,rock4_y,bullet_x+25,bullet_y)<100:
        score+=1
        fire=False
        rock4_x=random.randint(10,670)
        rock4_y=random.randint(-100,-50)
        bullet_y=spaec_ship_position_y

# __________________________________________functions for showing astoroids__________________________________________
def astoroids():
    global rock1_x,rock1_y,rock2_x,rock2_y,rock3_x,rock3_y,rock4_x,rock4_y,plusbullets_y,plusbullets_x,vision_y,vision_x
    display.blit(rock1,(rock1_x,rock1_y))
    display.blit(rock2,(rock2_x,rock2_y))
    display.blit(rock4,(rock3_x,rock3_y))
    display.blit(rock3,(rock4_x,rock4_y))
    display.blit(plusbullets,(plusbullets_x,plusbullets_y))
    display.blit(vision,(vision_x,vision_y))
    # ___________________all astoroid speeds______________________
    rock1_y+=10
    rock2_y+=10
    rock3_y+=10
    rock4_y+=10
    plusbullets_y+=10
    vision_y+=10

    if rock1_y>950:
        rock1_x=random.randint(10,600)
        rock1_x=400
        rock1_y=random.randint(-40,-20)

    if rock2_y>950:
        rock2_x=random.randint(10,600)
        rock2_y=random.randint(-300,-200)

    if rock3_y>950:
        rock3_x=random.randint(10,600)
        rock3_y=-40

    if rock4_y>950:
        rock4_x=random.randint(10,600)
        rock4_y=-random.randint(-100,-50)

    if plusbullets_y>950:
        plusbullets_x=random.randint(10,600)
        plusbullets_y=-1000

    if vision_y>950:
        vision_x=random.randint(10,600)
        vision_y=random.randint(-6000,-3000)

# ____________________________________________function for showing text____________________________________
font = pygame.font.Font("comic.ttf", 35)
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    display.blit(screen_text, [x,y])
# _________________________function for reset the default valuse after starting new game___________________
def reset():
    global running,fire,remove_bullets,score,bullets,spaec_ship_position_x,spaec_ship_position_y,rock1_x,rock1_y,rock2_x,rock2_y,rock3_x,rock3_y,rock4_x,rock4_y,plusbullets_y,plusbullets_x,bullet_y,bullet_x,spaec_ship_v,vision_ON
    running=True
    fire=False
    remove_bullets=1
    score=0
    bullets=5
    spaec_ship_position_x=250
    spaec_ship_position_y=800

    rock1_x=random.randint(10,630)
    rock1_y=-500
    rock2_x=random.randint(10,630)
    rock2_y=0
    rock3_x=random.randint(10,630)
    rock3_y=-500
    rock4_x=random.randint(10,630)
    rock4_y=0
    plusbullets_x=200
    plusbullets_y=200

    bullet_y=spaec_ship_position_y
    bullet_x=spaec_ship_position_x+45
    spaec_ship_v=0
    vision_ON=False
# _______________________________________________game start display______________________________________
def gamestart():    
    pygame.mixer.music.load("bgsound.mp3")
    pygame.mixer.music.play(loops=-1)
    running=True
    while running:
        display.blit(startup,(0,0))
        display.blit(spaceShip,(spaec_ship_position_x,spaec_ship_position_y))
        text_screen("Welcome to Alien Run 3",(0,255,0),140,300)
        text_screen("Hit Space Bar To Play",(0,255,0),140,380)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    gameloop()
        pygame.display.update()

# __________________________________________gameover start display______________________________________
def gameover():    
    time.sleep(1)
    running=True
    while running:
        display.blit(startup,(0,0))
        display.blit(spaceShip,(spaec_ship_position_x,spaec_ship_position_y))
        text_screen("Game over",(255,0,0),240,300)
        text_screen(f"score:{score}",(0,255,0),250,360)
        text_screen("Hit Space Bar To Play again",(0,255,0),100,430)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    reset()
                    gamestart()
        pygame.display.update()
# _____________________________________________main game loop_____________________________________________
def gameloop():
    global spaec_ship_position_x,fire,bullets,spaec_ship_v,remove_bullets,bullet_x,bullet_y,vision_ON,vision_TimeOut
    fire=False

    running=True
    while running:
        background()
        if spaec_ship_position_x<15:
            spaec_ship_v=0
        if spaec_ship_position_x>515:
            spaec_ship_v=0
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE or event.key==pygame.K_a :
                    fire=True
                    if bullets!=0:
                        bullets-=remove_bullets
                if event.key==pygame.K_UP:
                    fire=True
                    if bullets!=0:
                        bullets-=remove_bullets
                elif event.key==pygame.K_RIGHT:
                    spaec_ship_v=10
                elif event.key==pygame.K_LEFT:
                    spaec_ship_v=-10
                elif event.key==pygame.K_DOWN:
                    spaec_ship_v=0
        # _______________for bullet firring____________
        if not fire:
            bullet_x=spaec_ship_position_x+45
            bullet_y=spaec_ship_position_y+20
        if bullets>0:
            if fire:
                display.blit(bullet ,(bullet_x+30,bullet_y))
                display.blit(bullet ,(bullet_x-30,bullet_y))
                bullet_y-=30
                if bullet_y<-20:
                    bullet_y=spaec_ship_position_y
                    fire=False
        # _________________________________________________
        display.blit(spaceShip,(spaec_ship_position_x,spaec_ship_position_y))

        astoroids()
        # ________________ score and bullets_______________
        text_screen(f"score {score}",(255,0,255),10,10)
        text_screen(f"bullets {bullets}",(255,0,255),250,10)
        # ______________moveing the spaceship_____________
        spaec_ship_position_x+=spaec_ship_v
        # ________________________________________________
        colliding()

        bulletCollision()
        # _____________________ for vision ability_____________________________
        if vision_ON:
            vision_TimeOut-=1
            pygame.draw.rect(display, ((255,255,255)),(rock1_x,rock1_y,100,100), 5)
            pygame.draw.rect(display, ((255,0,255)),(rock3_x,rock3_y,100,100), 5)
            pygame.draw.rect(display, ((0,255,0)),(rock4_x,rock4_y,100,100), 5)
            pygame.draw.rect(display, ((0,255,255)),(rock2_x,rock2_y,200,200), 5)
            if vision_TimeOut==0:
                vision_ON=False
                vision_TimeOut=200

        clock.tick(25)
        pygame.display.update()
if __name__ == '__main__':
    gamestart ()    
