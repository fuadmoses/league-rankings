import unittest
from league_rankings.match_parser import MatchParser
from league_rankings.league import League


class TestLeagueRankings(unittest.TestCase):

    def test_match_parser(self):
        sample_match = "Lions 3, Snakes 2"
        match = MatchParser(sample_match)
        self.assertIsNotNone(match)
        self.assertEqual(match.team_a, "Lions")
        self.assertEqual(match.team_b, "Snakes")
        self.assertEqual(match.score_a, 3)
        self.assertEqual(match.score_b, 2)

    def test_process_match_win(self):
        sample_match = "Lions 3, Snakes 2"
        match = MatchParser(sample_match)
        league = League()
        league.process_match(match)
        self.assertIsNotNone(league.ranking_table)
        self.assertDictEqual(league.ranking_table, {"Lions": 3, "Snakes": 0})

    def test_process_match_draw(self):
        sample_match = "Lions 3, Snakes 3"
        match = MatchParser(sample_match)
        league = League()
        league.process_match(match)
        self.assertIsNotNone(league.ranking_table)
        self.assertDictEqual(league.ranking_table, {"Lions": 1, "Snakes": 1})

    def test_process_match_loss(self):
        sample_match = "Lions 2, Snakes 3"
        match = MatchParser(sample_match)
        league = League()
        league.process_match(match)
        self.assertIsNotNone(league.ranking_table)
        self.assertDictEqual(league.ranking_table, {"Lions": 0, "Snakes": 3})


if __name__ == '__main__':
    unittest.main()
