#Classe pai - (super classe) - generalista
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
    
    def evaluate(self, note):
        self.totalEvaluation += note
        self.evaluators += 1
    
    def average(self):
        print(f"Média do jogo {self.name}: {self.totalEvaluation / self.evaluators}")

#Classe derivada (subclasse) - especializada
class SinglePlayerGame(Game):
    def __init__(self, name="", yearLaunch=0,note=0, storyLine=""):
        super().__init__(name, yearLaunch, multiplayer=False, note=note)
        self.storyLine = storyLine
    
    def technical_sheet(self):
        super().technical_sheet()
        print(f"Enredo: {self.storyLine}\n")

mult_game = Game("Fortnite", 2017, True, 8.5)
mult_game.technical_sheet()

sing_game = SinglePlayerGame("God of War", 2018, 9.5, "A história de Kratos e seu filho Atreus em uma jornada pela mitologia nórdica.")
sing_game.technical_sheet()
        