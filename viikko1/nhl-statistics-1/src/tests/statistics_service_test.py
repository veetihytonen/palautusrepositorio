import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def playerEqu(self, p1, p2):
        return (
            p1.name == p2.name and
            p1.team == p2.team and
            p1.goals == p2.goals and
            p1.assists == p2.assists
        )

    def test_search_yields_correct_player(self):
        player = self.stats.search("Semenko")
        assertion = Player("Semenko", "EDM", 4, 12)
        
        assert isinstance(player, Player)
        self.assertTrue(self.playerEqu(player, assertion))

    def test_invalid_search_returns_none(self):
        self.assertIsNone(self.stats.search("WrongName"))

    def test_team_search_is_correct(self):
        real_players = [
            Player("Semenko", "EDM", 4, 12),
            Player("Kurri",   "EDM", 37, 53),
            Player("Gretzky", "EDM", 35, 89)
        ]

        result = self.stats.team("EDM")
        assert isinstance(result, list)
        assert len(real_players) == len(result)
        for real, tested in zip(real_players, result):
            self.assertTrue(self.playerEqu(real, tested))

    def test_invalid_team_yields_empty_list(self):
        result = self.stats.team("Invalid")

        assert isinstance(result, list)
        assert len(result) == 0
    
    def test_top_returns_right_amount(self):
        result = self.stats.top(3)
        print(result)
        self.assertEqual(len(result), 3)
    
    def test_top_returns_right_players(self):
        real_players = [
            Player("Gretzky", "EDM", 35, 89),
            Player("Lemieux", "PIT", 45, 54),
            Player("Yzerman", "DET", 42, 56),
        ]
        result = self.stats.top(3)

        for real, tested in zip(real_players, result):
            self.assertTrue(self.playerEqu(real, tested))