from player_reader import PlayerReader
from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

class StatisticsService:
    def __init__(self, player_reader: PlayerReader):
        self.__reader = player_reader

        self.__players = self.__reader.get_players()

    def getSorter(self, key: SortBy):
        match key:
            case SortBy.POINTS:
                return lambda player: player.points
            case SortBy.GOALS:
                return lambda player: player.goals
            case SortBy.ASSISTS:
                return lambda player: player.assists
    
    def search(self, name):
        for player in self.__players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self.__players
        )

        return list(players_of_team)

    def top(self, how_many: int, key: SortBy = None):
        # metodin käyttämä apufufunktio voidaan määritellä näin
        if not key:
            sorter = lambda player: player.points + player.assists
        else:
            sorter = self.getSorter(key)

        sorted_players = sorted(
            self.__players,
            reverse=True,
            key=sorter
        )

        result = []
        i = 0
        while i < how_many:
            result.append(sorted_players[i])
            i += 1

        return result
