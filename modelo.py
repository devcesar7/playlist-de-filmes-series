class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
    @property
    def likes(self):
        return self._likes
    def dar_like(self):
        self._likes += 1
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()



# Classe que representa um filme
class Filme (Programa):
    # Construtor da classe Filme
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao      # Armazena a duração do filme em minutos



# Classe que representa uma série (estrutura parecida com Filme)
class Serie (Programa):
    # Construtor da classe Serie
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas   # Armazena o número de temporadas



# Criação de um objeto da classe Filme
vingadores = Filme("vingadores - guerra infinita", 2018, 160)
# Adiciona um like ao filme
vingadores.dar_like()
# Exibe as informações do filme formatadas
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} - Likes: {vingadores.likes}')



# Criação de um objeto da classe Serie
atlanta = Serie("atlanta", 2018, 2)
# Adiciona dois likes à série
atlanta.dar_like()
atlanta.dar_like()
# Exibe as informações da série formatadas
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}')