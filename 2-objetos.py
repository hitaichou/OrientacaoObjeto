class Game:
    name = ""
    yearLaunch = 0
    multiplayer = False
    note = 0.0
#Classe?
#é um molde, um modelo, uma estrutura para criar objetos
#classe = conjunto de atributos e métodos 
#atributos = características
#métodos = ações

#Objeto:
#é criar um objeto a partir de uma classe (que é um molde)
#objeto = instância da classe
   
#primeiro jogo
game1 = Game()
game1.name = "The Legend of Zelda: Breath of the Wild"
game1.yearLaunch = 2017
game1.multiplayer = False
game1.note = 9.5

#segundo jogo
game2 = Game()
game2.name = "Fortnite"
game2.yearLaunch = 2017
game2.multiplayer = True
game2.note = 8.0


#f = formatted string (string formatada) - 
# permite inserir variáveis dentro da string de forma mais prática
print("###Dados do Jogo###")
print(f"Nome do jogo: {game1.name} \nAno de lançamento: {game1.yearLaunch}")
print(f"Nome do jogo: {game2.name} \nAno de lançamento: {game2.yearLaunch}")