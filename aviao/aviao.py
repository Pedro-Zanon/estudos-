#troca de assento de aviao

import random

class Avião():

    def __init__(self):
        self.assentos_disponiveis = []
        self.todos_assentos = []
        self.rsalvos = []
    def iniciar_voo(self):
        letras = ["A", "B", "C"]
        # Gera assentos no formato A-1, B-2, C-3, A-4, etc.
        # (i-1) % 3 gera a sequência de índices 0, 1, 2, 0, 1, 2... para as letras.
        self.todos_assentos = [f"{letras[(i-1) % 3]}-{i}" for i in range(1, 101)]
        # -----------------------------------------------------------

        # Sorteia 5 assentos que estarão livres para este voo
        self.assentos_disponiveis = random.sample(self.todos_assentos, 5)
        
        # Atribui um dos assentos disponíveis ao usuário
        self.meu_assento = random.choice(self.assentos_disponiveis)
        self.assentos_disponiveis.remove(self.meu_assento) # Remove o assento do usuário da lista de disponíveis  
    def cadastro(self):
        criarlogin = input("Digite seu nome: ")
        criarsenha = input("Digite sua senha: ")
        self.registro = {"login": criarlogin, "senha": criarsenha}
        if self.registro not in self.rsalvos:
          self.rsalvos.append(self.registro)
          print("Cadastro feito com sucesso!")
          
        elif self.registro in self.rsalvos:
          print("Você ja possui cadastro!")
        login = input("login: ")
        senha = input("senhas: ")
        if login != self.registro["login"] or senha != self.registro["senha"]:
         print("Login ou senha errados. Tente novamente!")
        else:
         print("--- Bem-vindo a bordo! ---")
         print(f"Seu assento é o: {self.meu_assento}")
        # Inicia o processo de troca
        self.trocar_assento(self.meu_assento)

    def trocar_assento(self, meu_assento_atual):
        
        while True:
            troca = input("\nQuer trocar o seu assento? (Sim/Não): ").strip().upper()
            
            if troca == "SIM":
                if not self.assentos_disponiveis:
                    print("Desculpe, não há outros assentos disponíveis para troca.")
                    break 

                print("\nEstes são os assentos disponíveis para troca:")
                print(self.assentos_disponiveis)

                while True:
                    novo_assento = input("Escolha seu novo assento: ").strip().upper()
                    
                    if novo_assento in self.assentos_disponiveis:
                        self.assentos_disponiveis.remove(novo_assento)
                        self.assentos_disponiveis.append(meu_assento_atual)
                        meu_assento_atual = novo_assento
                        
                        print(f"\nSeu assento foi trocado e agora é o {meu_assento_atual}")
                        print("Lista de assentos livres foi atualizada:", self.assentos_disponiveis)
                        break 
                    else:
                        print("Opção inválida! Por favor, escolha um assento da lista.")
                
                break

            elif troca == "NÃO":
                break

            else:
                print("Opção inválida! Por favor, responda com 'Sim' ou 'Não'.")

        print(f"\nO seu assento final é o {meu_assento_atual}. Tenha uma ótima viagem!")

# Instanciando e executando o programa
c = Avião()
c.iniciar_voo()
c.cadastro()