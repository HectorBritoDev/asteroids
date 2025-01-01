import pygame

from constants import *
from player import Player


def main():
    print('Starting asteroids!')
    print("Screen width:",SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    pygame.init()
    time = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = time.tick(60) / 1000
        screen.fill((0, 0, 0))

        for entity in updatable:
            entity.update(dt)

        for entity in drawable:
            entity.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()