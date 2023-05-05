import pygame
import sys

class Game:
    def __init__(self):
        # Initialization
        pygame.init()

        # Constants
        self.WIDTH, self.HEIGHT = 800, 600
        self.PADDLE_WIDTH, self.PADDLE_HEIGHT = 15, 100
        self.BALL_SIZE = 15
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.BLACK = (0, 0, 0)

        # Create the screen
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Red "SOX" Pong')

    def home_page(self, classic_pong, team_pong):
        # Code for home_page method

        if classic_rect.collidepoint(x, y):
            classic_pong.start_game()
        if team_rect.collidepoint(x, y):
            team_pong.start_game()
