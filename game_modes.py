import pygame
import sys
import random


class ClassicPong:
    """
    Class representing the Classic Pong game mode.
    """

    def __init__(self, game):
        """
        Initialize the Classic Pong game mode.

        :param game: Game instance
        """
        self.game = game

    def start_game(self):
        """
        Start the Classic Pong game mode and handle game logic.
        """
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
        BLACK = (183, 36, 36)  # The Background of the screen

        # Create the screen
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Pong")

        # Create paddles, ball, and score
        paddle_a = pygame.Rect(
            10, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT
        )
        paddle_b = pygame.Rect(
            WIDTH - 20, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT
        )
        ball = pygame.Rect(
            WIDTH // 2 - BALL_SIZE // 2,
            HEIGHT // 2 - BALL_SIZE // 2,
            BALL_SIZE,
            BALL_SIZE,
        )

        color_ball = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )

        paddle_a_color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )

        paddle_b_color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )

        # Scores
        score_a = 0
        score_b = 0

        # Ball velocity
        ball_speed_x = BALL_SPEED
        ball_speed_y = BALL_SPEED

        # Function to display scores
        def display_scores():
             """
            Display the score of the game

            Returns:
                The score will return in a form of score: "number digits"
            """
            font = pygame.font.Font(None, 36)
            text = font.render(f"{score_a} - {score_b}", True, WHITE)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 10))

        # Timer
        start_ticks = pygame.time.get_ticks()

        # Function to display timer
        def display_timer(elapsed_time):
            """
            Display the timer as it deceased.

            args:
                elapsed_time: the amount of tim

            Returns:
                displays timer in in form of 0:00 minutes:seconds and its the amount of time left
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
            Indicating the game is over and report the score the player receive.

            Returns:
                "Game over " will be display following by the score report in form of score: number digits
            """
            font = pygame.font.Font(None, 48)

            game_over_text = font.render("GAME OVER", True, WHITE)
            game_over_rect = game_over_text.get_rect(
                center=(WIDTH // 2, HEIGHT // 2 - 50)
            )
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
                color_ball = (
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255),
                )

                paddle_a_color = (
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255),
                )
                paddle_b_color = (
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255),
                )

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
            pygame.draw.rect(screen, paddle_a_color, paddle_a)
            pygame.draw.rect(screen, paddle_b_color, paddle_b)
            pygame.draw.ellipse(screen, color_ball, ball)
            pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

            # Display scores
            display_scores()

            # Display timer
            display_timer(elapsed_time)

            # Update display
            pygame.display.flip()
            pygame.time.delay(20)


class TeamPong:
    """
    Class representing the Classic Pong game mode.
    """

    def __init__(self, game):
        """
        Initialize the Team Pong game mode.

        :param game: Game instance
        """
        self.game = game

    def start_game(self):
        """
        Start the Team Pong game mode and handle game logic.
        """
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
        pygame.display.set_caption("Pong")

        # Create paddles, ball, and score
        paddle_a = pygame.Rect(
            10, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT
        )
        paddle_b = pygame.Rect(
            WIDTH - 20, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT
        )
        ball = pygame.Rect(
            WIDTH // 2 - BALL_SIZE // 2,
            HEIGHT // 2 - BALL_SIZE // 2,
            BALL_SIZE,
            BALL_SIZE,
        )

        # Score
        score = 0

        # Ball velocity
        ball_speed_x = BALL_SPEED
        ball_speed_y = BALL_SPEED

        # Function to display score
        def display_score():
            """
            Display the score of the game everytime the pong hits the paddle.

            Returns:
                The score will return in a form of score: "number digits"
            """
            font = pygame.font.Font(None, 36)
            text = font.render(f"Score: {score}", True, WHITE)
            screen.blit(text, (WIDTH - 120, 10))

        # Function to display game over
        def display_game_over():
            """
            Indicating the game is over and report the score the player receive.

            Returns:
                "Game over " will be display following by the score report in form of score: number digits
            """
            font = pygame.font.Font(None, 48)

            game_over_text = font.render("GAME OVER", True, WHITE)
            game_over_rect = game_over_text.get_rect(
                center=(WIDTH // 2, HEIGHT // 2 - 50)
            )
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
                ball_speed_x = ball_speed_x * 1.2 if score % 5 == 4 else ball_speed_x
                ball_speed_y = ball_speed_y * 1.2 if score % 5 == 4 else ball_speed_y
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
