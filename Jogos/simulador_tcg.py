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

# 3. Entrada de dados dos Usuários


print("    Atributos da Carta 1   ")
nome1 = input("Nome da Carta 1: ")
hp1 = ler_status_valido("HP da Carta 1: ")
ataque1 = ler_status_valido("Pontos de Ataque da Carta 1: ")
carta1 = Carta(nome1, hp1, ataque1)

print("\n   Atributos da Carta 2    ")
nome2 = input("Nome da Carta 2: ")
hp2 = ler_status_valido("HP da Carta 2: ")
ataque2 = ler_status_valido("Pontos de Ataque da Carta 2: ")
carta2 = Carta(nome2, hp2, ataque2)

print("\n    A batalha irá começar!  ")
time.sleep(1)

# 4. Sorteio de quem começa


jogadores = [carta1, carta2]
atacante = random.choice(jogadores)
defensor = carta2 if atacante == carta1 else carta1

print(f"\n🎲 Sorteio realizado! {atacante.nome} joga primeiro.")
print("--- A Batalha Vai Começar! ---")
time.sleep(1)

# 5. Loop do Jogo (Turnos)


turno = 1
while carta1.esta_viva() and carta2.esta_viva():
    print(f"\n⚡ Rodada {turno} ⚡")
    print(f"{carta1.nome} ({carta1.hp} HP) VS {carta2.nome} ({carta2.hp} HP)")
    print("-" * 30)
    time.sleep(1)
      
    
    print(f"⚔️  {atacante.nome} ataca {defensor.nome} causando {atacante.ataque} de dano!")
    defensor.hp -= atacante.ataque
    
    
    if not defensor.esta_viva():
        defensor.hp = 0  
        break

    atacante, defensor = defensor, atacante
    
    turno += 1
    time.sleep(1.5)

    turno += 1
    time.sleep(1.5)

# 6. Fim de Jogo e Anúncio do Vencedor


print("\n" + "="*30)
print("       Fim Da Batalha!        ")
print("="*30)

if carta1.esta_viva():
    print(f"🏆 Vencedor: {carta1.nome} com {carta1.hp} de HP restante!")
else:
    print(f"🏆 Vencedor: {carta2.nome} com {carta2.hp} de HP restante!")
