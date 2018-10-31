import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
dark_red = (200, 0, 0)
blue = (0, 0, 255)
dark_blue = (0, 0, 200)

car_width = 64



pause = False


gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("BittiRalli")
clock = pygame.time.Clock()

carImg = pygame.image.load("racecar.png")
pygame.display.set_icon(carImg)  # changes the icon top left

def blocks_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))


def blocks(blockx, blocky, blockw, blockh, color):  # draw a block to dodge
    pygame.draw.rect(gameDisplay, color, [blockx, blocky, blockw, blockh])



def car(x,y):  # shows the car on screen
    gameDisplay.blit(carImg,(x,y))  # draws to the background, what and where? carImg to x,y

# upleft corner is 0,0. as you add to x you move to right. add To y you move down.

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf", 70)
    TextSurface, TextRectangle = text_objects(text, largeText)  # run text_objects function
    TextRectangle.center = ((display_width / 2), (display_height/2))
    gameDisplay.blit(TextSurface, TextRectangle)  # to draw to screen
    pygame.display.update()

    time.sleep(2)
    game_loop()  # start game loop again

def crash():
# crash function, when crashed, it displays a screen with two buttons play again and quit.

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font("freesansbold.ttf", 70)
        TextSurface, TextRectangle = text_objects("You Crashed", largeText)  # run text_objects function
        TextRectangle.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurface, TextRectangle)

        button("Play again", 150, 450, 100, 50, dark_blue, blue, "play")
        button("Quit", 550, 450, 100, 50, dark_red, red, "quit")



        pygame.display.update()
        clock.tick(15) # wait 15 secs

def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    print(mouse)  # debugging

    click = pygame.mouse.get_pressed()


    # makes buttons more interactive
    if x+w> mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        # plays different action according to the button
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
    textSurf, textRect = text_objects(msg , smallText)  # smallText = font
    textRect.center = ((x + (w / 2)), (y + (h / 2)))  # x + half of the width , y + half of the height
    gameDisplay.blit(textSurf, textRect)

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
        largeText = pygame.font.Font("freesansbold.ttf", 70)
        TextSurface, TextRectangle = text_objects("Paused", largeText)  # run text_objects function
        TextRectangle.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurface, TextRectangle)

        button("Continue", 150, 450, 100, 50, dark_blue, blue, "unpause")
        button("Quit", 550, 450, 100, 50, dark_red, red, "quit")






        pygame.display.update()
        clock.tick(15) # wait 15 secs


# runs one time before game starts
def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font("freesansbold.ttf", 70)
        TextSurface, TextRectangle = text_objects("Bitti Ralli", largeText)  # run text_objects function
        TextRectangle.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurface, TextRectangle)

        button("Play", 150, 450, 100, 50, dark_blue, blue, "play")
        button("Quit", 550, 450, 100, 50, dark_red, red, "quit")






        pygame.display.update()
        clock.tick(15) # wait 15 secs

def game_loop():
    global pause

    x = (display_width * 0.45)
    y = (display_height * 0.7)

    dx = 0
    dy = 0

    block_startx = random.randrange(0, display_width)
    block_starty = -600
    block_speed = 4
    block_width = 100
    block_height = 100
    dodged = 0

    gameExit = False

    # main game loop
    while not gameExit:

        for event in pygame.event.get():  # event handler
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx -= 5
                    print("x is:" + str(x))  # debugging also
                if event.key == pygame.K_RIGHT:
                    dx += 5
                    print("x is:" + str(x))  # debugging also
                if event.key == pygame.K_UP:
                    dy -= 4
                    print("y is: " + str(y))
                if event.key == pygame.K_DOWN:
                    dy += 4
                    print("y is: " + str(y))
                if event.key == pygame.K_p:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    dx = 0
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    dy = 0

        x += dx
        y += dy
       # print(event) # <- debugging purposes
        gameDisplay.fill(white)

        # drawing
        blocks(block_startx, block_starty, block_width, block_height, black)
        block_starty += block_speed  # makes block move!
        car(x,y)
        blocks_dodged(dodged)

        # collision detection car and side borders
        if x > display_width - 55 or x < -10:
            crash()  # run crash() function
        # collision between car and bottom border and upper
        if y > 444:
            y = 444
        if y < 28:
            y = 28

        # when block goes off the screen, print another at random x
        if block_starty > display_height:
            block_starty = 0 - block_height
            block_startx = random.randrange(0, display_width)
            dodged += 1
            block_speed += 0.25
            print(block_speed)
            print("block's x is: " + str(block_startx))

        # collision detection between block and car
        if block_startx < x + car_width and block_startx + block_width > x:
            crash()




        pygame.display.update()
        clock.tick(60) # fps


#uninitialize Pygame
game_intro()
game_loop()
pygame.quit()
quit()