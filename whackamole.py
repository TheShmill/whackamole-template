import pygame
import random


def draw_board(screen):
    pygame.draw.line(screen, "black", (0, 0), (0, 640))
    pygame.draw.line(screen, "black", (32, 0), (32, 640))
    pygame.draw.line(screen, "black", (64, 0), (64, 640))
    pygame.draw.line(screen, "black", (96, 0), (96, 640))
    pygame.draw.line(screen, "black", (128, 0), (128, 640))
    pygame.draw.line(screen, "black", (160, 0), (160, 640))
    pygame.draw.line(screen, "black", (192, 0), (192, 640))
    pygame.draw.line(screen, "black", (224, 0), (224, 640))
    pygame.draw.line(screen, "black", (256, 0), (256, 640))
    pygame.draw.line(screen, "black", (288, 0), (288, 640))
    pygame.draw.line(screen, "black", (320, 0), (320, 640))
    pygame.draw.line(screen, "black", (352, 0), (352, 640))
    pygame.draw.line(screen, "black", (384, 0), (384, 640))
    pygame.draw.line(screen, "black", (416, 0), (416, 640))
    pygame.draw.line(screen, "black", (448, 0), (448, 640))
    pygame.draw.line(screen, "black", (480, 0), (480, 640))
    pygame.draw.line(screen, "black", (512, 0), (512, 640))
    pygame.draw.line(screen, "black", (544, 0), (544, 640))
    pygame.draw.line(screen, "black", (576, 0), (576, 640))
    pygame.draw.line(screen, "black", (608, 0), (608, 640))
    pygame.draw.line(screen, "black", (640, 0), (640, 640))
    #pygame.draw.line(screen, "black", (0, 0), (512, 512))
    pygame.draw.line(screen, "black", (0, 32), (640, 32))
    pygame.draw.line(screen, "black", (0, 64), (640, 64))
    pygame.draw.line(screen, "black", (0, 96), (640, 96))
    pygame.draw.line(screen, "black", (0, 128), (640, 128))
    pygame.draw.line(screen, "black", (0, 160), (640, 160))
    pygame.draw.line(screen, "black", (0, 192), (640, 192))
    pygame.draw.line(screen, "black", (0, 224), (640, 224))
    pygame.draw.line(screen, "black", (0, 256), (640, 256))
    pygame.draw.line(screen, "black", (0, 288), (640, 288))
    pygame.draw.line(screen, "black", (0, 320), (640, 320))
    pygame.draw.line(screen, "black", (0, 352), (640, 352))
    pygame.draw.line(screen, "black", (0, 384), (640, 384))
    pygame.draw.line(screen, "black", (0, 416), (640, 416))
    pygame.draw.line(screen, "black", (0, 448), (640, 448))
    pygame.draw.line(screen, "black", (0, 480), (640, 480))
    pygame.draw.line(screen, "black", (0, 512), (640, 512))
    pygame.draw.line(screen, "black", (0, 544), (640, 544))
    pygame.draw.line(screen, "black", (0, 576), (640, 576))
    pygame.draw.line(screen, "black", (0, 608), (640, 608))
    pygame.draw.line(screen, "black", (0, 640), (640, 640))




def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        mole_X = 0
        mole_Y = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x,y = event.pos
                    if mole_X <= x < mole_X + 32 and mole_Y <= y < mole_Y + 32:
                        mole_X = random.randrange(0, 19) * 32
                        mole_Y = random.randrange(0, 15) * 32
            screen.fill("light green")
            draw_board(screen)
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_X, mole_Y)))
            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()
if __name__ == "__main__":
    main()
