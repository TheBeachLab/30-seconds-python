import pygame

# initialize game engine
pygame.init()
# load icon
icon = pygame.image.load('image.png')
# set screen width/height, icon and caption
size = [640, 480]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('My Game')
pygame.display.set_icon(icon)
# initialize clock. used later in the loop.
clock = pygame.time.Clock()

# Loop until the user clicks close button
done = False
while done == False:
    # write event handlers here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # write game logic here

    # clear the screen before drawing
    screen.fill((255, 255, 255))
    # write draw code here

    # display what’s drawn. this might change.
    pygame.display.update()
    # run at 20 fps
    clock.tick(20)

# close the window and quit
pygame.quit()
