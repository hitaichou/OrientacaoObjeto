class Game:
    """
    -------------------------------------------------
    trocando os atributos abaixo por um construtor
    -------------------------------------------------
    name = ""
    yearLaunch = 0
    multiplayer = False
    note = 0.0
    """
    #método construtor
    #método especial que é chamado quando um objeto é criado
    #é usado para inicializar os atributos do objeto
    #self = referência ao próprio objeto
    #pode receber parâmetros para inicializar os atributos
    #nesse caso, estamos inicializando todos os atributos
    def __init__(self, name="", yearLaunch=0, multiplayer=False, note=0.0):
        self.name = name
        self.yearLaunch = yearLaunch
        self.multiplayer = multiplayer
        self.note = note
        self.totalEvaluation = 0
        self.evaluators = 0
    
    #Método __str__
    #método especial que retorna uma representação em string do objeto
    #quando você tenta imprimir o objeto, esse método é chamado automaticamente
    #você pode personalizar o que será retornado
    #nesse caso, estamos retornando o nome do jogo
    def __str__(self):
        return f"Nome do jogo: {self.name}\nAno de lançamento: {self.yearLaunch} \nMultiplayer: {self.multiplayer} \nNota: {self.note}"
    
    #método technical_sheet
    #é um método que exibe todas as informações do objeto
    #nesse caso, estamos exibindo todas as informações do jogo
    #você pode chamar esse método para exibir as informações do jogo
    def technical_sheet(self):
        print("###Dados do Jogo###")
        print(f"Nome do jogo: {self.name}")
        print(f"Ano de lançamento: {self.yearLaunch}")
        print(f"Multiplayer: {self.multiplayer}")
        print(f"Nota: {self.note}\n")    
    #método evaluate
    #é um método que recebe uma nota e adiciona ao total de avaliações
    #e incrementa o número de avaliadores
    
    def evaluate(self, note):
        self.totalEvaluation += note
        self.evaluators += 1
    #método average
    #é um método que calcula a média das avaliações
    #e exibe a média das avaliações
    def average(self):
        print(f"Média do jogo {self.name}: {self.totalEvaluation / self.evaluators}")
    
    
game1 = Game("The Legend of Zelda: Breath of the Wild", 2017, False, 9.5)
game2 = Game("Fortnite", 2017, True, 8.0)

game1.technical_sheet()
game2.technical_sheet()
game1.evaluate(9)
game1.evaluate(7.5)
game1.average()
game2.evaluate(6)
game2.evaluate(8)
game2.average()