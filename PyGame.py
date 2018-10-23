import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)

bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

red = (200, 0, 0)
green = (0, 200, 0)


car_width = 90

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Racing Game")
clock = pygame.time.Clock()
carImg = pygame.image.load("nimetön3.png")

pause = False

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text, (0,0))


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])



def car(x,y):
    gameDisplay.blit(carImg, (x, y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf", 100)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

def crash():
    message_display("You crashed!")

def button(msg, x,y,w,h,ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()



    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == "play":
                game_loop()
            elif action == "quit":
                pygame.quit()
                quit()
            elif action == "unpause":
                unpause()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font("freesansbold.ttf", 100)
        TextSurf, TextRect = text_objects("Hiukan Racey", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!", 150, 450, 100, 50, green, bright_green, "play")
        button("Quit!",550, 450, 100, 50, red, bright_red, "quit")





        pygame.display.update()
        clock.tick(15)
def unpause():
    global pause
    pause = False

def paused():


    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font("freesansbold.ttf", 100)
        TextSurf, TextRect = text_objects("Pause", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        button("Continue", 150, 450, 100, 50, green, bright_green, "unpause")
        button("Quit!",550, 450, 100, 50, red, bright_red, "quit")





        pygame.display.update()
        clock.tick(15)


def game_loop():
    global pause

    x = (display_width * 0.45)


    y = (display_height * 0.6)

    dx = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed  = 4
    thing_width = 100
    thing_height = 100
    dodged = 0



    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx -= 5
                elif event.key == pygame.K_RIGHT:
                    dx += 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    dx = 0




        x += dx

        gameDisplay.fill(white)


        things(thing_startx, thing_starty, thing_width, thing_height, black)




        thing_starty += thing_speed
        car(x, y)
        things_dodged(dodged)

        if x > ( display_width - car_width) or x < -10:
            crash()


        if thing_starty > display_height:
            thing_starty = -400
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 0.25
            print(thing_speed)


# detection between car and thing
        if y < thing_starty+thing_height:
            print("y-crossover")


            if thing_startx<x+car_width and thing_startx+thing_width>x:
                print("x crossover")
                crash()


        pygame.display.update()
        clock.tick(60)
game_intro()
game_loop()
pygame.quit()
quit()


# kuva 100,160
