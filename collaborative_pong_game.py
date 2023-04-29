import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
BALL_SIZE = 15
PADDLE_SPEED = 7
BALL_SPEED = 5
GAME_TIME = 120000  # 2 minutes in milliseconds

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')

# Create paddles, ball, and score
paddle_a = pygame.Rect(10, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle_b = pygame.Rect(WIDTH - 20, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

# Score
score = 0

# Ball velocity
ball_speed_x = BALL_SPEED
ball_speed_y = BALL_SPEED

# Function to display score
def display_score():
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (WIDTH - 120, 10))
    
# Function to display game over
def display_game_over():
    font = pygame.font.Font(None, 48)

    game_over_text = font.render("GAME OVER", True, WHITE)
    game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(game_over_text, game_over_rect)

    score_text = f"Score: {score}"
    score_surface = font.render(score_text, True, WHITE)
    score_rect = score_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))
    screen.blit(score_surface, score_rect)

    pygame.display.flip()
    pygame.time.delay(3000)
    
# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle_a.top > 0:
        paddle_a.y -= PADDLE_SPEED
    if keys[pygame.K_s] and paddle_a.bottom < HEIGHT:
        paddle_a.y += PADDLE_SPEED
    if keys[pygame.K_UP] and paddle_b.top > 0:
        paddle_b.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and paddle_b.bottom < HEIGHT:
        paddle_b.y += PADDLE_SPEED

    # Ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y = -ball_speed_y
        
    # Ball collision with paddles and scoring
    if ball.colliderect(paddle_a) or ball.colliderect(paddle_b):
        ball_speed_x = -ball_speed_x
        score += 1

    # Ball out of bounds and game over
    if ball.left <= 0 or ball.right >= WIDTH:
        display_game_over()
        pygame.quit()
        sys.exit()
        
    # Drawing objects
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle_a)
    pygame.draw.rect(screen, WHITE, paddle_b)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))
    
    # Display score
    display_score()

    # Update display
    pygame.display.flip()
    pygame.time.delay(20)
