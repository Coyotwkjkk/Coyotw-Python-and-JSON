import json
import os

agenda = []

def salvar_agenda():
    with open("agenda.json", "w", encoding="utf-8") as arquivo:
        json.dump(agenda, arquivo, indent=4, ensure_ascii=False)

def carregar_agenda():
    global agenda

    if os.path.exists("agenda.json"):
        try:
            with open("agenda.json", "r", encoding="utf-8") as arquivo:
                agenda = json.load(arquivo)
        except:
            agenda = []

def adcionar_pessoas():
    pessoa = {}

    nome = input("Adcionar nome de usuario: ")
    data = input("Adcionar data do usuario: ")

    pessoa["Nome"] = nome
    pessoa["Data"] = data

    agenda.append(pessoa)

    for chave, valor in pessoa.items():
        print(f"{chave}: {valor}")

    input("\nPressione ENTER para continuar...")
    salvar_agenda()

def remover_pessoas():
    leitura = len(agenda)

    if leitura == 0:
        print("A lista está vazia.")
    else:
        

        for position, pessoa in enumerate(agenda, start=1):
            nome = pessoa["Nome"]
            data = pessoa["Data"]
            print(f"{position} - Nome: {nome} // Data: {data}")
            print()
        try:
            escolher_remover = int(input("Quem deseja remover? Digite a posição: "))

            if escolher_remover < 1 or escolher_remover > leitura:
                print("Posição inexsitente, tente novamente.")

            else:

                agenda.pop((escolher_remover - 1))
                print("Usuario removido com sucesso.")
                input("\nPressione ENTER para continuar...")
                salvar_agenda()

        except ValueError:
            print("Opção inválida, tente novamente.") 

def listar_pessoas():
    leitura = len(agenda)
    
    if leitura == 0:
        print("A lista está vazia.")
        input("\nPressione ENTER para continuar...")

    else:    
        for position, pessoa in enumerate(agenda, start=1):
            nome = pessoa["Nome"]
            data = pessoa["Data"]
            print(f"{position} - Nome: {nome} // Data: {data}")
            input("\nPressione ENTER para continuar...")
            print()
def main():

    carregar_agenda()

    while True: 
        print("Menu Iniciar: \n")
        print("1 - Adicionar usuario na lista")
        print("2 - Listar usuarios na lista")
        print("3 - Remover usuario da lista")
        print("4 - Sair\n")

        try:

            op = int(input("Escolha uma opção: 1/2/3 ou 4: "))
            print()

            
            if op == 1:
                adcionar_pessoas()
                
            elif op == 2:
                listar_pessoas()

            elif op == 3:
                remover_pessoas()

            elif op == 4:
                print("Saindo...")
                break

        except ValueError:
                print("Escolha invalida, tente novamente.")

if __name__ == "__main__" :
    main()