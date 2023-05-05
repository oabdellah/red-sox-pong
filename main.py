import pygame
from game import Game
from game_modes import ClassicPong, TeamPong


def main():
    """
    Main function to run the Red "SOX" Pong game.
    """
    game = Game()
    classic_pong = ClassicPong(game)
    team_pong = TeamPong(game)

    while True:
        game.home_page(classic_pong, team_pong)


if __name__ == "__main__":
    main()
