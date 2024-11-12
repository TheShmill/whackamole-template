import pygame
import random

from pygame.examples.cursors import image


def pick_random_spot():
    row = random.randrange(0, 16)
    col = random.randrange(0, 20)
    return (col, row)

def draw_grid(screen):
    length = 32
    width = 32
    LINE_COLOR = (0,0,0)
    LINE_WIDTH = 1

    #Draw horizontal lines
    for i in range(1, 16):
        pygame.draw.line(
            screen, LINE_COLOR,
            (0, i*length),
            (640, i*length),
            LINE_WIDTH
        )

    #Draw vertical lines
    for i in range(1, 20):
        pygame.draw.line(
            screen, LINE_COLOR,
            (i*width,0),
            (i*width, 512),
            LINE_WIDTH
        )

def draw_image(screen, image, x, y):
    screen.blit(image, image.get_rect(topleft=(x,y)))

def image_is_click(image_position, x, y):
    x_top_left = image_position[0] * 32
    y_top_left = image_position[1] * 32
    return x_top_left < x < x_top_left+32 and y_top_left < y < y_top_left + 32

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True

        mole_position = (0,0)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and image_is_click(mole_position, event.pos[0], event.pos[1]):
                    mole_position = pick_random_spot()

            screen.fill("light green")
            draw_grid(screen)
            draw_image(screen, mole_image, mole_position[0]*32, mole_position[1]*32)

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
