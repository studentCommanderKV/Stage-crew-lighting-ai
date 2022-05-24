import pygame
from light import Light

size = (500, 500)
WIN = pygame.display.set_mode(size)

def draw(items:list = []):
    if len(items) > 0:
        for item in items:
            item.draw(WIN)

    pygame.display.update()


def main():
    lights = [
        Light(100, 100, 10)
    ]

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        draw(lights)

    pygame.quit()

if __name__ == "__main__":
    main()
