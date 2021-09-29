if __name__ == '__main__':
    from match_parser import MatchParser
else:
    from league_rankings.match_parser import MatchParser


class League:
    def __init__(self):
        self.ranking_table = dict()

    def process_match(self, match: MatchParser = None):
        """
        Updates the ranking table by processing the match
        """
        if match.score_a == match.score_b:
            self.ranking_table[match.team_a] = self.ranking_table.get(match.team_a, 0) + 1
            self.ranking_table[match.team_b] = self.ranking_table.get(match.team_b, 0) + 1
        elif match.score_a > match.score_b:
            self.ranking_table[match.team_a] = self.ranking_table.get(match.team_a, 0) + 3
            self.ranking_table[match.team_b] = self.ranking_table.get(match.team_b, 0)
        elif match.score_a < match.score_b:
            self.ranking_table[match.team_b] = self.ranking_table.get(match.team_b, 0) + 3
            self.ranking_table[match.team_a] = self.ranking_table.get(match.team_a, 0)

    def print_rankings(self):
        """
        Prints the ranking table in highest ranking and alphabetical order
        """
        # sort alphabetically, regardless of case sensitivity
        rankings_sorted = sorted(self.ranking_table.items(), key=lambda item: str(item[0]).lower())
        # sort by highest ranking
        rankings_sorted = dict(sorted(rankings_sorted, key=lambda item: item[1], reverse=True))
        idx = 1
        for name, points in rankings_sorted.items():
            print(f"{idx}. {name}, {points} {'pt' if points == 1 else 'pts'}")
            idx = idx + 1
