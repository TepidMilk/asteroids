import pygame
from circleshape import *
from player import *
from constants import *


pygame.init
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))
clock = pygame.time.Clock()
dt = 0

def main():
    player = Player(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    while True:
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player.draw(screen)
        tick = clock.tick(60)
        dt = tick / 1000
        pygame.display.flip()



if __name__ == "__main__":
    main()