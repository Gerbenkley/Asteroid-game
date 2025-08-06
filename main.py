import sys
import pygame

from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from circleshape import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        dt = clock.tick(60) / 1000

        #MAIN LOOP
        screen.fill(0)

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collisioncheck(player):
                print("Game over!")
                sys.exit()

        for drawables in drawable:
            drawables.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
