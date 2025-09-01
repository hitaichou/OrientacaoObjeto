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
    
    
game1 = Game("The Legend of Zelda: Breath of the Wild", 2017, False, 9.5)
game2 = Game("Fortnite", 2017, True, 8.0)
game3 = Game("Minecraft", 2011, True, 9.0)

game1.technical_sheet()
game2.technical_sheet()
game1.evaluate(9)
game1.evaluate(7.5)
game1.average()
game2.evaluate(6)
game2.evaluate(8)
game2.average()
game3.technical_sheet()
game3.evaluate(10)
game3.average()


print(f"Total de jogos criados: {Game.total_games}")