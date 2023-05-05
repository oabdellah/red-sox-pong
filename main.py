import pygame
import sys
from game import Game
from game_modes import ClassicPong, TeamPong

if __name__ == "__main__":
    game = Game()
    classic_pong = ClassicPong(game)
    team_pong = TeamPong(game)
    game.home_page(classic_pong, team_pong)
