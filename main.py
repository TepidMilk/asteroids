import pygame
from constants import *

pygame.init
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))
clock = pygame.time.Clock()
dt = 0

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        tick = clock.tick(60)
        dt = tick / 1000


if __name__ == "__main__":
    main()