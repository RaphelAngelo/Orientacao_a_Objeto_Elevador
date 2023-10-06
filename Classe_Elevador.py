# 1. Crie uma classe para representar um Elevador com os seguintes atributos
# - andar atual (terreo = 0)
# - quantidade de andares
# - capacidade (qtd de pessoas que podem ter no elevador)
# - qtd pessoas (dentro do elevador)

# 2. Crie as seguintes funções pro elevador
# subir() -> sobe um andar (não pode passar do ultimo andar)
# descer() -> desce um andar (não pode passar do terreo)
# entrar(qtd) -> não pode ultrapassar a capacidade
# sair(qtd) -> não pode ficar com qtd pessoas negativa

class Elevador:
    def __init__(self, andar_atual, qtd_andares, capacidade, qtd_pessoas):
        self.andar_atual = andar_atual
        self.qtd_andares = qtd_andares
        self.capacidade = capacidade
        self.qtd_pessoas = qtd_pessoas

    # Métodos
    def subir(self):
        if self.andar_atual < self.qtd_andares:
            self.andar_atual += 1
            print('Subindo...')
            print(f'Andar atual: {self.andar_atual}')
        else:
            print('Você já esta no ultimo andar!')

    def descer(self):
        if self.andar_atual > 0:
            self.andar_atual -= 1
            print('Descendo...')
            print(f'Andar atual: {self.andar_atual}')
        else:
            print('Você está no térreo!')

    def entrar(self, n_pessoas):
        if self.qtd_pessoas + n_pessoas <= self.capacidade:
            self.qtd_pessoas += n_pessoas
            print('Entrando...')
            print(f'Quantidade de pessoas atual: {self.qtd_pessoas}')
        else:
            print('A capacidade não suporta essa quantidade!')

    def sair(self, n_pessoas):
        if self.qtd_pessoas - n_pessoas >= 0:
            self.qtd_pessoas -= n_pessoas
            print('Saindo...')
            print(f'Quandtidade de pessoas atual: {self.qtd_pessoas}')
        else:
            print('O valor não pode ser maior que a quantidade de pessoas!')


# Criar objeto?
plaza = Elevador(2, 10, 5, 3)
rio_mar = Elevador(3, 3, 6, 4)

# acessando um atributo de um objeto
print(f"Capaciade do Elevador plaza: {plaza.capacidade}")
plaza.subir()
rio_mar.descer()
rio_mar.descer()
rio_mar.entrar(2)
rio_mar.entrar(1)
rio_mar.sair(6)
rio_mar.sair(1)