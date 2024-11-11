import requests

class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']
    
    def __str__(self):
        return f"{self.name:20}{self.team:5}{self.goals:3} + {self.assists:3} = {self.goals + self.assists}"

class PlayerReader:
    def __init__(self, url: str):
        self.url = url

    def get_players(self):
        response = requests.get(self.url).json()
        players = [Player(player_dict) for player_dict in response]

        return players
    

class PlayerStats:
    def __init__(self, reader: PlayerReader):
        self.reader = reader
        self.players = self.reader.get_players()

    def top_scorers_by_nationality(self, nationality: str):
        return sorted(list(filter(lambda player: player.nationality == nationality, self.players)), key=lambda player: player.goals + player.assists, reverse=True)
    