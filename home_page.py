import pygame
import sys

# Home page function
def home_page():
    """
    Displaying the color of the screen as well as variable for the pongs and paddle that we want to display in the home screen. 

    Returns:
        the color of the screen, the paddle, the pong ball
    """
    pygame.init()
    
    # Constants
    WIDTH, HEIGHT = 800, 600
    PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
    BALL_SIZE = 15

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
    font_small = pygame.font.Font(None, 36)

    title_text = font_large.render("Welcome to Red SOX Pong!", True, RED)
    choose_text = font_medium.render("Choose Game Mode", True, WHITE)
    classic_text = font_small.render("Classic Pong", True, WHITE)
    team_text = font_small.render("Team Pong", True, WHITE)

    # Paddles and ball
    paddle_a = pygame.Rect(10, HEIGHT // 2 - PADDLE_HEIGHT // 2 - 50, PADDLE_WIDTH, PADDLE_HEIGHT)
    paddle_b = pygame.Rect(WIDTH - 20, HEIGHT // 2 - PADDLE_HEIGHT // 2 + 50, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = pygame.Rect(WIDTH // 2 + 250, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

    # Main loop for the home page
    while True:
        screen.fill(BLACK)

        # Display text
        title_rect = title_text.get_rect(center=(WIDTH // 2, 50))
        screen.blit(title_text, title_rect)
        
        choose_rect = choose_text.get_rect(center=(WIDTH // 2, 250))
        screen.blit(choose_text, choose_rect)
        
        classic_rect = classic_text.get_rect(center=(WIDTH // 2, 350))
        team_rect = team_text.get_rect(center=(WIDTH // 2, 450))

        pygame.draw.rect(screen, WHITE, classic_rect.inflate(20, 10), 2)
        pygame.draw.rect(screen, WHITE, team_rect.inflate(20, 10), 2)
        
        screen.blit(classic_text, classic_rect)
        screen.blit(team_text, team_rect)

        # Draw paddles and ball
        pygame.draw.rect(screen, WHITE, paddle_a)
        pygame.draw.rect(screen, WHITE, paddle_b)
        pygame.draw.ellipse(screen, WHITE, ball)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if classic_rect.collidepoint(x, y):
                    # Classic Pong game mode
                    pong_game()
                if team_rect.collidepoint(x, y):
                    # Team Pong game mode
                    team_pong_game()

        pygame.display.flip()

if __name__ == "__main__":
    home_page()
