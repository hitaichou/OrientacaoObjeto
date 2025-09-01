class Game:
        
    total_games = 0 #Variavel de classe para contar o número de jogos criados
    def __init__(self, name="", yearLaunch=0, multiplayer=False, note=0.0):
        self.name = name
        self.yearLaunch = yearLaunch
        self.multiplayer = multiplayer
        self.note = note
        Game.total_games += 1 #Incrementa a variável de classe toda vez que um novo jogo é criado
        self.totalEvaluation = 0
        self.evaluators = 0
    
   
    def __str__(self):
        return f"Nome do jogo: {self.name}\nAno de lançamento: {self.yearLaunch} \nMultiplayer: {self.multiplayer} \nNota: {self.note}"
        
    def technical_sheet(self):
        print("###Dados do Jogo###")
        print(f"Nome do jogo: {self.name}")
        print(f"Ano de lançamento: {self.yearLaunch}")
        print(f"Multiplayer: {self.multiplayer}")
        print(f"Nota: {self.note}\n")    
    
#Composição
# Um estúdio de jogos pode ter vários jogos associados a ele.
# A classe GameStudio contém uma lista de objetos da classe Game.
# Isso representa a relação de composição, onde um estúdio "possui" vários jogos.

class GameStudio:
    def __init__(self, name=""):
        self.name = name
        self.games = [] #Lista para armazenar os jogos desenvolvidos pelo estúdio
    
    def add_game(self, game):
        self.games.append(game) #Adiciona um jogo à lista de jogos do estúdio
    
    def evaluate_studio_quality(self):
        total_notes = sum(game.note for game in self.games)
        total_games = len(self.games)
        if total_games == 0:
            print(f"O estúdio {self.name} não possui jogos para avaliação.")
        else:
            average_note = total_notes / total_games
            print(f"A média das notas dos jogos do estúdio {self.name} é: {average_note:.2f}")

game1 = Game("The Last of Us", 2013, False, 9.5)
game2 = Game("God of War", 2018, False, 9.7)
game3 = Game("Uncharted 4", 2016, False, 9.3)

studio = GameStudio("Naughty Dog") #Cria um estúdio de jogos
studio.add_game(game1)
studio.add_game(game2)
studio.add_game(game3)

studio.evaluate_studio_quality() #Avalia a qualidade do estúdio com base na média das notas dos jogos

for game in studio.games:
    game.technical_sheet()
    
        