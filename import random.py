import random

# --- Sistema de Inventário RPG ---

# Dicionário que armazena os itens da loja
itens_loja = {
    "Poção de Cura": {"preço": 20.00, "estoque": 10},
    "Espada": {"preço": 50.00, "estoque": 5},
    "Escudo": {"preço": 30.00, "estoque": 5},
}

# Jogador com atributos iniciais
class Jogador:
    def __init__(self, nome, dinheiro_inicial=100):
        self.nome = nome
        self.hp = 100
        self.ataque = 10
        self.defesa = 5
        self.inventario = []
        self.dinheiro = dinheiro_inicial  # Adicionando o dinheiro inicial do jogador

    def usar_item(self, item):
        if item == "Poção de Cura" and item in self.inventario:
            cura = random.randint(15, 30)
            self.hp += cura
            self.inventario.remove(item)
            print(f"{self.nome} usou {item} e curou {cura} de HP!")
        else:
            print(f"Você não tem {item} no inventário ou não pode usá-lo!")

    def adicionar_item(self, item):
        self.inventario.append(item)
        print(f"{self.nome} pegou {item}!")

    def remover_item(self, item):
        if item in self.inventario:
            self.inventario.remove(item)
            print(f"{self.nome} removeu {item} do inventário!")

    def exibir_status(self):
        print(f"\nStatus de {self.nome}:")
        print(f"HP: {self.hp}, Ataque: {self.ataque}, Defesa: {self.defesa}")
        print(f"Dinheiro: R${self.dinheiro:.2f}")
        print(f"Inventário: {', '.join(self.inventario) if self.inventario else 'Nada'}\n")

# Função para exibir os itens da loja
def exibir_itens_loja():
    print("\nItens disponíveis na loja:")
    for item, info in itens_loja.items():
        print(f"{item} - Preço: R${info['preço']:.2f}, Estoque: {info['estoque']} unidades")
    print()

# Função para realizar a compra de um item
def comprar_item(jogador):
    exibir_itens_loja()
    item_escolhido = input("Digite o nome do item que deseja comprar: ")

    if item_escolhido in itens_loja:
        quantidade = int(input(f"Digite a quantidade de {item_escolhido} que deseja comprar: "))
        if itens_loja[item_escolhido]["estoque"] >= quantidade:
            total = quantidade * itens_loja[item_escolhido]["preço"]
            if jogador.dinheiro >= total:
                print(f"Total da compra: R${total:.2f}")
                confirmacao = input("Deseja confirmar a compra? (s/n): ")

                if confirmacao.lower() == "s":
                    # Simula a compra e atualiza o inventário
                    itens_loja[item_escolhido]["estoque"] -= quantidade
                    jogador.dinheiro -= total
                    for _ in range(quantidade):
                        jogador.adicionar_item(item_escolhido)
                    print(f"{quantidade}x {item_escolhido} foi comprado(a)!")

                else:
                    print("Compra cancelada.")
            else:
                print(f"Você não tem dinheiro suficiente! Seu saldo: R${jogador.dinheiro:.2f}.")
        else:
            print(f"Estoque insuficiente. Apenas {itens_loja[item_escolhido]['estoque']} unidades disponíveis.")
    else:
        print("Item não encontrado na loja.")

# Função para aplicar uma promoção
def sortear_promocao():
    item_sorteado = random.choice(list(itens_loja.keys()))
    desconto = random.randint(10, 50)  # Desconto entre 10% e 50%
    itens_loja[item_sorteado]["preço"] *= (1 - desconto / 100)
    print(f"\nPromoção! O item {item_sorteado} está com {desconto}% de desconto!\n")

# --- Sistema de História Interativa ---

# Função que gera a introdução da história
def gerar_introducao():
    introducoes = ["Era uma vez", "Há muito tempo atrás", "Num reino distante"]
    return random.choice(introducoes)

# Função que gera o desenvolvimento da história
def gerar_desenvolvimento():
    desenvolvimentos = ["um valente cavaleiro", "uma destemida guerreira", "um bravo guerreiro",
                        "uma poderosa feiticeira", "um sábio mago"]
    return random.choice(desenvolvimentos)

# Função que gera o final da história
def gerar_final():
    finais = ["enfrentando dragões ferozes.", "derrotando um terrível vilão.",
              "descobrindo um tesouro escondido.", "salvando o reino da escuridão.",
              "encontrando um amor verdadeiro."]
    return random.choice(finais)

# Função principal que gera toda a história
def gerar_historia(jogador):
    introducao = gerar_introducao()
    desenvolvimento = gerar_desenvolvimento()
    final = gerar_final()

    historia = f"{introducao} {desenvolvimento} {final}"

    print("\nAventura Iniciada!")
    print(f"\n{historia}")
    print("\nO que você deseja fazer agora?")
    print("1. Continuar a aventura")
    print("2. Voltar para a cidade e comprar itens")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        print("\nVocê continua sua jornada...")
        jogador.exibir_status()
        confrontar_dragao(jogador)
    elif escolha == "2":
        print("\nVocê decide voltar para a cidade e fazer compras.")
        menu(jogador)
    else:
        print("\nOpção inválida. Tentando novamente...")
        gerar_historia(jogador)

def confrontar_dragao(jogador):
    print("\nVocê se aproxima de uma caverna escura. Um dragão gigantesco aparece diante de você!")
    print("Ele solta uma rajada de fogo! O que você fará?")

    dano_dragao = random.randint(20, 50)  # O dragão causa um dano entre 20 e 50

    # Se o jogador não tiver escudo, ele morre imediatamente
    if "Escudo" not in jogador.inventario:
        print(f"\n{jogador.nome} não possui um escudo! O dragão atacou com força total!")
        jogador.hp = 0  # O jogador morre imediatamente
        jogador.exibir_status()
        print(f"\n{jogador.nome} morreu! Fim de jogo.")
        return

    # Se o jogador tiver escudo, ele toma menos dano
    else:
        print("\nVocê usou o escudo para se proteger do fogo! O dano foi reduzido!")
        dano_dragao -= 20  # O escudo reduz o dano em 20

    # Verifica se o jogador ainda está vivo após o ataque do dragão
    if dano_dragao > jogador.hp:
        jogador.hp = 0  # O jogador morre se o dano for maior que seu HP
    else:
        jogador.hp -= dano_dragao

    print(f"\nO dragão atacou! Você tomou {dano_dragao} de dano!")
    jogador.exibir_status()

    if jogador.hp <= 0:
        print(f"\n{jogador.nome} não resistiu ao ataque do dragão e morreu. Fim de jogo.")
        return

    # O jogador pode atacar ou usar uma poção
    print("\nAgora você tem algumas opções para reagir.")
    print("1. Usar a Espada para atacar o dragão")
    print("2. Usar uma Poção de Cura")
    
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        print(f"\nVocê ataca o dragão com sua espada!")
        dano_ataque = random.randint(15, 30)  # O dano do ataque varia
        print(f"\nVocê causou {dano_ataque} de dano ao dragão!")
        print("\nO dragão está enfraquecendo, você conseguiu derrotá-lo!")
    elif escolha == "2":
        if "Poção de Cura" in jogador.inventario:
            jogador.usar_item("Poção de Cura")
            print("\nVocê usou uma Poção de Cura e agora está pronto para atacar!")
            dano_ataque = random.randint(15, 30)
            print(f"\nVocê causou {dano_ataque} de dano ao dragão!")
        else:
            print("\nVocê não tem Poções de Cura no inventário!")
    else:
        print("\nOpção inválida. Você perdeu sua chance de reagir!")
        jogador.hp -= 10
        print(f"\nVocê perdeu 10 de HP por hesitar. O dragão está atacando!")
    
    jogador.exibir_status()
    if jogador.hp <= 0:
        print(f"\n{jogador.nome} morreu! Fim de jogo.")
        return

# --- Menu Principal ---

def menu(jogador):
    while True:
        print("=== Sistema de Inventário RPG ===")
        print("1. Comprar item")
        print("2. Ver status do jogador")
        print("3. Usar item")
        print("4. Sortear promoção")
        print("5. Iniciar nova aventura")
        print("6. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            comprar_item(jogador)
        elif opcao == "2":
            jogador.exibir_status()
        elif opcao == "3":
            item_escolhido = input("Digite o nome do item que deseja usar: ")
            jogador.usar_item(item_escolhido)
        elif opcao == "4":
            sortear_promocao()
        elif opcao == "5":
            gerar_historia(jogador)
        elif opcao == "6":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.\n")

# Função principal para iniciar o jogo
def main():
    print("Bem-vindo ao RPG de Inventário e Aventura!")
    nome = input("Digite o nome do seu personagem: ")
    dinheiro_inicial = float(input("Digite a quantidade inicial de dinheiro: R$"))
    jogador = Jogador(nome, dinheiro_inicial)
    jogador.exibir_status()

    while True:
        menu(jogador)

if __name__ == "__main__":
    main()
