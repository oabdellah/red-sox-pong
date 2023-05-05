import unittest
from game import Game
from game_modes import ClassicPong, TeamPong

import pygame
from pygame.locals import *


class TestPong(unittest.TestCase):
    def test_classic_pong_init(self):
        game = Game()
        classic_pong = ClassicPong(game)
        self.assertIsNotNone(classic_pong.game)
        self.assertEqual(
            classic_pong.score_a, 0
        )  # Check the score of player a in the beginning
        self.assertEqual(
            classic_pong.score_b, 0
        )  # Check the score of player b in the beginning
        self.assertEqual(classic_pong.ball_speed_x, 5)  # Check the speed of the ball
        self.assertEqual(classic_pong.ball_speed_y, 5)  # Check the speed of the ball

    def test_team_pong_init(self):
        game = Game()
        team_pong = TeamPong(game)
        self.assertIsNotNone(team_pong.game)
        self.assertEqual(team_pong.score, 0)  # Check the score in the beginning is 0
        self.assertEqual(team_pong.ball_speed_x, 5)  # Check the ball speed
        self.assertEqual(team_pong.ball_speed_y, 5)  # Check the ball speed

    def test_game_init(self):
        game = Game()
        self.assertEqual(game.WIDTH, 800)  # Check the game board width
        self.assertEqual(game.HEIGHT, 600)  # Check the height of the board
        self.assertEqual(game.PADDLE_WIDTH, 15)  # Check the paddle width
        self.assertEqual(game.PADDLE_HEIGHT, 100)  # Check the paddle height
        self.assertEqual(game.BALL_SIZE, 15)  # Check the size of the ball


if __name__ == "__main__":
    unittest.main()
