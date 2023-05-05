import pygame
import sys

# Home page function
def home_page():
    pygame.init()
    
    # Constants
    WIDTH, HEIGHT = 800, 600

    # Colors
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)

    # Create the screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Red "SOX" Pong')

    # Font and text
    font_large = pygame.font.Font(None, 72)
    font_medium = pygame.font.Font(None, 48)

    title_text = font_large.render("Welcome to Red", True, WHITE)
    sox_text = font_large.render("SOX", True, RED)
    pong_text = font_large.render("Pong!", True, WHITE)

    choose_text = font_medium.render("Choose Game Mode", True, WHITE)
    classic_text = font_medium.render("Classic Pong", True, WHITE)
    team_text = font_medium.render("Team Pong", True, WHITE)

    # Main loop for the home page
    while True:
        screen.fill(BLACK)

        # Display text
        screen.blit(title_text, (WIDTH // 2 - 200, 50))
        screen.blit(sox_text, (WIDTH // 2 + 10, 50))
        screen.blit(pong_text, (WIDTH // 2 - 30, 120))
        screen.blit(choose_text, (WIDTH // 2 - 120, 250))
        screen.blit(classic_text, (WIDTH // 2 - 130, 350))
        screen.blit(team_text, (WIDTH // 2 - 80, 450))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if WIDTH // 2 - 130 <= x <= WIDTH // 2 + 130 and 350 <= y <= 390:
                    # Classic Pong game mode
                    pong_game()
                if WIDTH // 2 - 80 <= x <= WIDTH // 2 + 80 and 450 <= y <= 490:
                    # Team Pong game mode
                    team_pong_game()

        pygame.display.flip()

if __name__ == "__main__":
    home_page()
