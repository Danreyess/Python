class Game:
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre
        self.available = True

class Player:
    def __init__(self, name):
        self.name = name
        self.rented_games = []

class GameStore:
    def __init__(self):
        self.players = []
        self.games = []

    def add_game(self, title, genre):
        game = Game(title, genre)
        self.games.append(game)

    def add_player(self, name):
        player = Player(name)
        self.players.append(player)

    def show_games(self):
        for game in self.games:
            status = "Available" if game.available else "Not available"
            print(f"{game.title}: {status}")

    def rent_game(self, player_name, title):
        for player in self.players:
            if player.name == player_name:
                for game in self.games:
                    if game.title == title:
                        game.available = False
                        print(f"{player.name}: rented {game.title}")
                        return
                    else:
                        print(f"{game.title}: not available")
        print("Game not found")

    def return_games(self, player_name, title):
        for player in self.players:
            if player.name == player_name:
                for game in self.games:
                    if game.title == title:
                        game.available = True
                        print(f"{player.name}: returned {game.title}")
                        return
                    else:
                        print(f"{player.name}: did not rented {game.title}")
        print("Player not found")

game1 = GameStore()
game1.add_game("League of legends", "Moba")
game1.add_game("GTA 5", "Open world")
game1.add_player("Daniel")
game1.rent_game("Daniel", "GTA 5")
game1.show_games()




