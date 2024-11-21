import pygame
import random
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    #Method for splitting asteroids when hit
    def split(self):

        """always destroy object hit by shot then 
        if the asteroid was "small" end method
        """
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        #random angle between 20 and 50 degrees
        random_angle = random.uniform(20,50)

        #create 2 new angles to adjust velocity of new asteroids
        angle1 = self.velocity.rotate(random_angle)
        angle2 = self.velocity.rotate(-random_angle)
        
        #new radius for split asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        #create 2 new asteroids instances
        self.split1 = Asteroid(self.position.x, self.position.y, new_radius)
        self.split2 = Asteroid(self.position.x, self.position.y, new_radius)
        
        #adjust velocity of new asteroids
        self.split1.velocity = angle1 * 1.2
        self.split2.velocity = angle2 * 1.2

