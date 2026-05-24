import time
import random

# 1. Criação da estrutura da Carta


class Carta:
    def __init__(self, nome, hp, ataque):
        self.nome = nome
        self.hp = int(hp)
        self.ataque = int(ataque)

    def esta_viva(self):
        return self.hp > 0


# 2. validação dos valores inserido pelo usuário        
        
def ler_status_valido(mensagem_input):
    while True:
        entrada = input(mensagem_input)
        
        
        if not entrada.isdigit():
          print("❌ Erro: Por favor, digite apenas números inteiros positivos.")
          continue
        
        valor = int(entrada)
        
        if valor<=0:  
          print("❌ Erro: O valor deve ser maior que zero!")
          continue
            
        return valor
