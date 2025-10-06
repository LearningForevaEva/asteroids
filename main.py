import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
BLACK = (0, 0, 0)
x = SCREEN_WIDTH / 2
y = SCREEN_HEIGHT / 2

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
AsteroidField.containers = (updatable,)
Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
player = Player(x, y)
asteroidfield = AsteroidField()

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(SCREEN_WIDTH)
    print(SCREEN_HEIGHT)
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(BLACK)
        updatable.update(dt)
        for draw_able in drawable:
            draw_able.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
