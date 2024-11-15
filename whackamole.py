import pygame
import random
def draw_grid(screen):
    i,j = 0,0
    while i <= 640:
        pygame.draw.line(screen, "black", (i, 0), (i, 512))
        i += 32
    while j <= 512:
        pygame.draw.line(screen, "black", (0, j), (640, j))
        j += 32

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        mole_image = pygame.image.load("mole.png")
        clock = pygame.time.Clock()
        running = True
        screen = pygame.display.set_mode((640, 512))
        screen.fill("light green")
        draw_grid(screen)

        mole_x, mole_y = 10, 10
        screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x,mole_y)))


        pygame.display.flip()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    mole_grid_x, mole_grid_y = mole_x // 32, mole_y // 32
                    mouse_grid_x, mouse_grid_y = mouse_x // 32, mouse_y // 32
                    if mole_grid_x == mouse_grid_x and mole_grid_y == mouse_grid_y:
                        mole_x = random.randrange(0, 640, 32)
                        mole_y = random.randrange(0, 512, 32)
                        screen.fill("light green")
                        draw_grid(screen)
                        screen.blit(mole_image, (mole_x, mole_y))
                        pygame.display.flip()

            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
#position = event.pos
                    #position = (x//20,y/16)
                    #logic for when mole is clicked

                    #screen.fill("light green")
                    #draw_grid(screen)
                    #screen.blit(mole_image, mole_image.get_rect(topleft=(10, 10)))
                    #pygame.display.flip()