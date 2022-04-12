import unittest
from repositories.highscore_repository import HighscoreRepository

class TestHighscoreRepository(unittest.TestCase):
    def setUp(self):
        self.repo = HighscoreRepository()
        self.repo.add_event("Pekka", "WIN", "3x3")
        self.repo.add_event("Pekka", "WIN", "3x3")
        self.repo.add_event("Matti", "LOSE", "3x3")
    def test_get_highscores(self):
        test_highscore_list = [
            ("Pekka", 2),
            ("Matti", -1)
        ]
        self.assertEqual(self.repo.get_highscores("3x3"), test_highscore_list)

        