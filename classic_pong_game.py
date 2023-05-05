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

# Scores
score_a = 0
score_b = 0

# Ball velocity
ball_speed_x = BALL_SPEED
ball_speed_y = BALL_SPEED

# Function to display scores
def display_scores():
    """
    Displays the scores in the font choice and the location we decided. 
    Returns:
        It will display score in form of "number digit" - "number digit" 
    """
    font = pygame.font.Font(None, 36)
    text = font.render(f"{score_a} - {score_b}", True, WHITE)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 10))
    
# Timer
start_ticks = pygame.time.get_ticks()

# Function to display timer
def display_timer(elapsed_time):
    """
    Display the timer of the game decreasing over time given the Game time subtracting elapsed time.


    Args:
        elapsed_time: an int or float representing the amount time decreasing by miliseconds

    Returns:
        The amount of time in minutes and seconds the player has left in the game. 
    """
    remaining_time = (GAME_TIME - elapsed_time) // 1000
    minutes = remaining_time // 60
    seconds = remaining_time % 60
    timer_text = f"{minutes:02d}:{seconds:02d}"

    font = pygame.font.Font(None, 36)
    text = font.render(timer_text, True, WHITE)
    screen.blit(text, (WIDTH - 100, 10))
    
# Function to display game over and declare the winner
def display_game_over():
    """
    Onced there is no more time or the timer is 0:00, the screen will stop the whole game with game over indicated in the middle of the screen.

    Returns:
        returns the screen saying game over and whichever players wins depending on whichever players has the highest scores. 
    """
    font = pygame.font.Font(None, 48)

    game_over_text = font.render("GAME OVER", True, WHITE)
    game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(game_over_text, game_over_rect)

    if score_a > score_b:
        winner_text = "Player 1 Wins!"
    elif score_a < score_b:
        winner_text = "Player 2 Wins!"
    else:
        winner_text = "TIE!"

    winner_surface = font.render(winner_text, True, WHITE)
    winner_rect = winner_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))
    screen.blit(winner_surface, winner_rect)

    pygame.display.flip()
    pygame.time.delay(3000)
    
# Main game loop
while True:
    elapsed_time = pygame.time.get_ticks() - start_ticks

    if elapsed_time >= GAME_TIME:
        display_game_over()
        pygame.quit()
        sys.exit()

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

    # Ball collision with paddles
    if ball.colliderect(paddle_a) or ball.colliderect(paddle_b):
        ball_speed_x = -ball_speed_x

    # Ball out of bounds and scoring
    if ball.left <= 0:
        score_b += 1
        ball.x = WIDTH // 2 - BALL_SIZE // 2
        ball.y = HEIGHT // 2 - BALL_SIZE // 2
        ball_speed_x = -ball_speed_x
    elif ball.right >= WIDTH:
        score_a += 1
        ball.x = WIDTH // 2 - BALL_SIZE // 2
        ball.y = HEIGHT // 2 - BALL_SIZE // 2
        ball_speed_x = -ball_speed_x

    # Drawing objects
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle_a)
    pygame.draw.rect(screen, WHITE, paddle_b)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Display scores
    display_scores()
    
    # Display timer
    display_timer(elapsed_time)

    # Update display
    pygame.display.flip()
    pygame.time.delay(20)
