import pygame
# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# Call this function so the Pygame library can initialize itself
pygame.init()
# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 800])
# This sets the name of the window
pygame.display.set_caption('Fly')
clock = pygame.time.Clock()
# update screen
pygame.display.update()
# Set positions of graphics
background_position = [0, 0]
# Load and set up graphics.
# background_image = pygame.image.load("saturn_family1.jpg").convert()
player_image = pygame.image.load("/Users/olexiyusov/Desktop/Game.png").convert()
# If the image does not have a transparent layer, then to install it,
# You must use the set_colorkey () method of the Surface class:
player_image.set_colorkey((0, 0, 0))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True          
    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    player_position = pygame.mouse.get_pos()
    x = player_position[0] - 20  # center image
    y = player_position[1] - 34
    # Copy image to screen:
    screen.fill((0, 0, 0))
    screen.blit(player_image, [x, y])
    pygame.display.flip()
    clock.tick(60)


pygame.quit() 