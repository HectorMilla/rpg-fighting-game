import pygame

pygame.init()

# set frame rate
clock = pygame.time.Clock()
fps = 60

# game window
bottom_panel = 150
screen_width = 800
screen_height = 400 + bottom_panel

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Battle")


# load images
# background image
background_img = pygame.image.load("img/background/background.png").convert_alpha()
background_img = pygame.transform.scale(
    background_img, (screen_width, screen_height - bottom_panel)
)

# panel image
panel_img = pygame.image.load("img/icons/panel.png").convert_alpha()


# function for drawing background
def draw_bg():
    screen.blit(background_img, (0, 0))


# function for drawing panel
def draw_panel():
    screen.blit(panel_img, (0, screen_height - bottom_panel))


run = True

while run:
    # set frames
    clock.tick(fps)
    # draw background
    draw_bg()
    # draw panel
    draw_panel()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
