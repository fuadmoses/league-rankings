import sys
if __name__ == '__main__':
    from league import League
    from match_parser import MatchParser
else:
    from league_rankings.league import League
    from league_rankings.match_parser import MatchParser


def calculate_rankings(file_path: str = ""):
    try:
        league = League()
        with open(file_path) as file:
            for line in file:
                match = MatchParser(line)
                league.process_match(match)
        league.print_rankings()
    except FileNotFoundError:
        if not file_path:
            print("Please specify a valid file")
        else:
            print("File not found. Please specify a valid file")


def main():
    file = sys.argv[1]
    calculate_rankings(file)


if __name__ == '__main__':
    main()
