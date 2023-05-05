import unittest
from game import Game
from game_modes import ClassicPong, TeamPong


class TestPong(unittest.TestCase):
    def test_classic_pong_init(self):
        game = Game()
        classic_pong = ClassicPong(game)
        self.assertIsNotNone(classic_pong.game)
        self.assertEqual(classic_pong.score_a, 0)
        self.assertEqual(classic_pong.score_b, 0)
        self.assertEqual(classic_pong.ball_speed_x, 5)
        self.assertEqual(classic_pong.ball_speed_y, 5)

    def test_team_pong_init(self):
        game = Game()
        team_pong = TeamPong(game)
        self.assertIsNotNone(team_pong.game)
        self.assertEqual(team_pong.score, 0)
        self.assertEqual(team_pong.ball_speed_x, 5)
        self.assertEqual(team_pong.ball_speed_y, 5)

    def test_game_init(self):
        game = Game()
        self.assertEqual(game.WIDTH, 800)
        self.assertEqual(game.HEIGHT, 600)
        self.assertEqual(game.PADDLE_WIDTH, 15)
        self.assertEqual(game.PADDLE_HEIGHT, 100)
        self.assertEqual(game.BALL_SIZE, 15)


if __name__ == "__main__":
    unittest.main()
