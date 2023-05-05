import pygame
import sys


class Game:
    """
    Class representing the Red "SOX" Pong game.
    """

    def __init__(self):
        """
        Initialize the game.
        """
        pygame.init()

        self.WIDTH, self.HEIGHT = 800, 600
        self.PADDLE_WIDTH, self.PADDLE_HEIGHT = 15, 100
        self.BALL_SIZE = 15
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.BLACK = (0, 0, 0)

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Red "SOX" Pong')

    def home_page(self, classic_pong, team_pong):
        """
        Display the home page of the game and handle user interactions.

        :param classic_pong: ClassicPong instance
        :param team_pong: TeamPong instance
        """
        running = True
        while running:
            self.screen.fill(self.BLACK)
            font_title = pygame.font.Font(None, 48)
            font_options = pygame.font.Font(None, 36)

            title_text = font_title.render(
                'Welcome to Red "SOX" Pong!', True, self.WHITE
            )
            title_rect = title_text.get_rect(
                center=(self.WIDTH // 2, self.HEIGHT // 2 - 100)
            )
            self.screen.blit(title_text, title_rect)

            classic_text = font_options.render("Classic Pong", True, self.WHITE)
            classic_rect = classic_text.get_rect(
                center=(self.WIDTH // 2, self.HEIGHT // 2)
            )
            self.screen.blit(classic_text, classic_rect)

            team_text = font_options.render("Team Pong", True, self.WHITE)
            team_rect = team_text.get_rect(
                center=(self.WIDTH // 2, self.HEIGHT // 2 + 50)
            )
            self.screen.blit(team_text, team_rect)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if classic_rect.collidepoint(x, y):
                        classic_pong.start_game()
                    if team_rect.collidepoint(x, y):
                        team_pong.start_game()
