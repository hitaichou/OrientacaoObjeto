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
    
    #Método __str__
    #método especial que retorna uma representação em string do objeto
    #quando você tenta imprimir o objeto, esse método é chamado automaticamente
    #você pode personalizar o que será retornado
    #nesse caso, estamos retornando o nome do jogo
    def __str__(self):
        return f"Nome do jogo: {self.name}\nAno de lançamento: {self.yearLaunch} \nMultiplayer: {self.multiplayer} \nNota: {self.note}"
    
    
game1 = Game("The Legend of Zelda: Breath of the Wild", 2017, False, 9.5)
game2 = Game("Fortnite", 2017, True, 8.0)
#print(game1)
#print(game2)

print("###Dados do Jogo###")
print(f"Nome do jogo: {game1.name} \nAno de lançamento: {game1.yearLaunch}")
print(f"Nome do jogo: {game2.name} \nAno de lançamento: {game2.yearLaunch}")