import pygame, random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white",  (self.position), self.radius, 2)
        
    def update(self, dt):    
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
    
        random_angle = random.uniform(20, 50)

        asteroid_split1 = self.velocity.rotate(random_angle)
        asteroid_split2 = self.velocity.rotate(-random_angle)
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        split_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        split_asteroid1.velocity = asteroid_split1 * 1.2
        split_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        split_asteroid2.velocity = asteroid_split2 * 1.2
        
