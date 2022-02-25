import os

class Game:
    def __init__(self, players, game_list):
        self.players = players
        self.die = Die()
        self.game_list = game_list
        self.game_list.append(self)
    def run_game(self):
        finshed = False
        while not finshed:
            for player in self.players:
                for i in range(3):
                    roll = self.die.roll_die()
                    player.increase_position(roll)
                player.score += player.position
                if player.score >= 1000:
                    loser = min(self.players, key=lambda x: x.score)
                    print(loser.score * self.die.roll)
                    return

class Player:
    def __init__(self, position):
        self.position = position
        self.score = 0

    def increase_position(self, increase):
        self.position = 10 if (self.position + increase) % 10 == 0 else (self.position + increase) % 10

class Die:
    def __init__(self):
        self.roll = 0
    def roll_die(self):
        self.roll += 1

        return 100 if self.roll % 100 == 0 else self.roll % 100

if __name__ == "__main__":
    with open(os.path.dirname(__file__) + "/input.txt") as f:
        players = [Player(int(f.readline().strip()[-1])) for _ in range(2)]

    games = []

    game = Game(players, games)
    game.run_game()
