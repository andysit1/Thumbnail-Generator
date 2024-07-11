

"""
probably not needed file, just for displaying what we're looking at for longer durations...
"""


#things to know

#screen shotting -> pygame.image.save(screen,"screenshot.jpg")

import pygame

# pygame setup
pygame.init()



screen = pygame.display.set_mode((1280, 720)) #ideal size for youtube thumbnail
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")



    #grab video frame place in the center of the screen / frame

    #apply transformation to avatar and sizing to avatar
      #base on location scale scale the video

    #apply text in the center

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()