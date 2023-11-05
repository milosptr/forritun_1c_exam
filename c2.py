# Höfundur: Milos Petrovic
# Dagsetning: 31.10.2023
# Verkefni: Forritun 1C - Spurning 2

class Player:

  def __init__(self, name: str, team: str, games: int, goals: int):
    self.name = name
    self.team = team
    self.games = games
    self.goals = goals

  def add_game(self, goals: str):
    self.games += 1
    self.goals += goals

  def average_score(self) -> float:
    return self.goals / self.games

  def __str__(self):
    return f'Player: {self.name}\nTeam: {self.team}\nGames: {self.games}\nGoals: {self.goals}\nAverage goals per game: {round(self.average_score(), 2)}'

class Team:

  def __init__(self, name: str):
    self.name = name
    self.players = []

  def add_player(self, player: Player):
    self.players.append(player)

  def goal_scorer(self):
    # return player with most goals
    # using lambda to get the goals of each player
    # and then getting the max value
    return max(self.players, key=lambda x: x.goals)

  def __str__(self):
    # join players with newline
    # mapping them with lambda to get their name
    players = '\n'.join(map(lambda x: x.name, self.players))
    return f'Team: {self.name}\n{players}'


def main():
    player1 = Player("Gunnar Jónsson", "Keflavík", 17, 3)
    print(player1)
    player2 = Player("Anna Sigurðardóttir", "Breiðablik", 14, 5)
    print(player2)
    player3 = Player("Guðmundur Einarsson", "Keflavík", 11, 4)
    print(player3)
    player4 = Player("Sigrún Kjartansdóttir", "Breiðablik", 21, 6)
    print(player4)

    player1.add_game(3)
    player2.add_game(6)

    keflavik = Team("Keflavík")
    keflavik.add_player(player1)
    keflavik.add_player(player3)
    print(keflavik)
    print(f'Goal scorer: {keflavik.goal_scorer().name}')

    breidablik = Team("Breiðablik")
    breidablik.add_player(player2)
    breidablik.add_player(player4)
    print(breidablik)
    print(f'Goal scorer: {breidablik.goal_scorer().name}')


main()
