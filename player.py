import pygame
from constants import *
from circleshape import *

class Player(CircleShape):
    timer = 0

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

        # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    #draws player to screen
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)


    #allow player to rotate on screen
    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    #allows player to move backwards and forwards
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    #allows player to spawn a shot object
    def shoot(self, dt):
        self.shot = Shot(self.position.x, self.position.y)
        self.shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOT_SPEED
        
    """allows player to update movement through key presses
    which call rotate, move, and shoot methods"""
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt) 
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if Player.timer <= 0:
                self.shoot(dt)
                Player.timer = PLAYER_SHOT_COOLDOWN
        Player.timer -= dt
    


#shot class to destroy asteroids
class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
    
    #draws shot to screen
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS, 2)

    #updates movement of shot 
    def update(self, dt):
        self.position += (self.velocity * dt)