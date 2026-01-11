import pygame

pygame.init

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Adding backround image")

background_image = pygame.transform.scale(
pygame.image.load("penguin.png").convert(),
(SCREEN_WIDTH, SCREEN_HEIGHT))

def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display_surface.blit(backround_image, (0, 0))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

    if __name__ == "__main__":
        game_loop()

    