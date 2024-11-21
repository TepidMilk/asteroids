
import sys
import pygame
from circleshape import *
from player import *
from constants import *
from asteroids import *
from asteroidfield import *

#initialize game
pygame.init

#set screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))

#set clock
clock = pygame.time.Clock()

#delta time
dt = 0

#set groups
updateable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroid = pygame.sprite.Group()
shot = pygame.sprite.Group()

#assign objects to groups
Player.containers = (updateable, drawable)
Asteroid.containers = (asteroid, updateable, drawable)
AsteroidField.containers = (updateable)
Shot.containers = (updateable, drawable, shot)

def main():
    
    #create player
    player = Player(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
    
    #set field for asteroids to spawn
    field = AsteroidField()
    
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    
    #start game loop
    while True:
        
        #fills screen with a black background
        screen.fill("black")
        
        #set framerate
        tick = clock.tick(60)
        dt = tick / 1000
        
        #allow for x out of program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #call groups
        for items in updateable:
            items.update(dt)
        for items in drawable:
            items.draw(screen)
        for asteroids in asteroid:
            if asteroids.collision(player):
                print("Game Over!")
                sys.exit()
            for shots in shot:
                if asteroids.collision(shots):
                    asteroids.split()
                    shots.kill()
            
        #update display surface
        pygame.display.flip()



if __name__ == "__main__":
    main()