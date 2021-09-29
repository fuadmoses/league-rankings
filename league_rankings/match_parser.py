class MatchParser:
    """
    Parsers a given match string eg. "Lions 3, Snakes 3" into a match object
    """
    team_a: str = None
    team_b: str = None
    score_a: int = 0
    score_b: int = 0

    def __init__(self, match_result: str = None):
        a, b = match_result.split(',')
        a = a.split(' ')
        b = b.split(' ')
        self.team_a = str(' ').join(a[:-1]).strip()
        self.score_a = int(a[-1])
        self.team_b = str(' ').join(b[:-1]).strip()
        self.score_b = int(b[-1])
