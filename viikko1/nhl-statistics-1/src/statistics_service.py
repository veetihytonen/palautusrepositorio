from player_reader import PlayerReader

class StatisticsService:
    def __init__(self, player_reader: PlayerReader):
        self.__reader = player_reader

        self.__players = self.__reader.get_players()

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

    def top(self, how_many):
        # metodin käyttämä apufufunktio voidaan määritellä näin
        def sort_by_points(player):
            return player.points

        sorted_players = sorted(
            self.__players,
            reverse=True,
            key=sort_by_points
        )

        result = []
        i = 0
        while i < how_many:
            result.append(sorted_players[i])
            i += 1

        return result
