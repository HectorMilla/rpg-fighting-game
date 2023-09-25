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


# fighter class
class Fighter:
    def __init__(self, x, y, name, max_hp, strenght, potions):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strenght
        self.start_potions = potions
        self.potions = potions
        self.alive = True
        img = pygame.image.load(f"img/{self.name}/idle/0.png")
        self.image = pygame.transform.scale(
            img, (img.get_width() * 3, img.get_height() * 3)
        )
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self):
        screen.blit(self.image, self.rect)


# create knight and bandit
knight = Fighter(200, 320, "knight", 30, 10, 3)
bandit1 = Fighter(550, 320, "bandit", 20, 6, 1)
bandit2 = Fighter(700, 320, "bandit", 10, 10, 1)

bandit_list = []
bandit_list.append(bandit1)
bandit_list.append(bandit2)

run = True

while run:
    # set frames
    clock.tick(fps)
    # draw background
    draw_bg()
    # draw panel
    draw_panel()
    # draw fighter
    knight.draw()
    # draw bandits
    for bandit in bandit_list:
        bandit.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
