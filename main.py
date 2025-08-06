import sys
import pygame

from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from circleshape import *
from shot import *

def main():
    #INIT PYGAME, CLOCK AND SCREEN
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    SCORING_SYSTEM = 0

    #GROUPS
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    #MAIN LOOP
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #CLOCK, SCREEN AND UPDATE
        dt = clock.tick(60) / 1000
        screen.fill(0)
        updatable.update(dt)

        #COLLISION CHECKS
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collisioncheck(shot):
                    asteroid.split()
                    shot.kill()
                    SCORING_SYSTEM += 1
                    print(f"SCORE: {SCORING_SYSTEM}")
            if asteroid.collisioncheck(player):
                print("Game over!")
                sys.exit()
        #DRAW
        for drawables in drawable:
            drawables.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
