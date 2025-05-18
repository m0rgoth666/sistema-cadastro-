import json
import os 

#Definicao do arquivo json
ARQUIVO = "dados_pessoais.json" #ARQUIVO variavel global, armazenando o valor "dados_pessoais.json"


# Função para carregar dados do arquivo json 
def carregar_dados():

    # Verifica se o arquivo existe. 
    if os.path.exists(ARQUIVO): 
           # Abre arquivo em modo de leitura
        with open(ARQUIVO, 'r') as arquivo:
           try: 
             # Tenta carregar os dados do arquivo JSON 
            return json.load(arquivo)  
           except json.JSONDecodeError:
               # Trata a exceção caso o arquivo JSON esteja vazio ou corrompido.
               print(f"  Arquivo JSON está vazio ou corrompido. Criando novo arquivo...")
               return [] # Retorna uma lista vazia 
    else:  
        # Senão retorna uma lista vazia se o arquivo não existir     
        return []         
    
# Função para salvar dados do arquivo json 
def salvar_dados(lista):
    with open(ARQUIVO, 'w') as arquivo:
        json.dump(lista, arquivo, indent = 4)

# Criando uma função de cadastro
def criar_cadastro(lista):   
    print("\n--- Novo Cadastro ---")    
    pessoa = {}
    pessoa['nome']  = input("NOME.: ").title()
    pessoa['sexo']  = input("SEXO.: ").title()
    pessoa['idade'] = input("IDADE: ")
    pessoa['email'] = input("EMAIL:").lower()
    lista.append(pessoa)# Novo cadastro adicionado a lista 
    print(f"Cadastro realizado com sucesso ")

# função para listar cadastros 
def lista_cadastros(lista): 
    # imprime o titulo da lista
    print("\n--- Lista de cadastros ---")

    # Verifica se a lista está vazia 
    if not lista: 
        # Caso a lista esteja vazia, imprime uma mensagem informando que não há cadastros
        print("Nenhum cadastro encontrado.")
    else: 
        # Caso a lista contenha cadastros, executa o loop abaixo
        # O loop percorre a lista de cadastros e imprime dados de cada pessoa   
        for i, pessoa in enumerate(lista, start=1):
            # Imprime as informações de cada cadastro
            # A função enumerate nos da dois valores
            # i - o indice (numero do cadastro)
            # pessoa - o dicionário contendo os dados de uma pessoa 
            # A partir disso, os dados são informados de cada pessoa 
            print(f"{i}. Nome: {pessoa['nome']} | Idade: {pessoa['idade']} | Sexo: {pessoa['sexo']} | Email: {pessoa['email']} ")    

    
def menu():

    lista = carregar_dados()
    
    while True: 
        print("\n--- Menu de Opções---")
        print("1. adicionar novo cadastro")
        print("2. lista de cadastros.")
        print("3. Salvar e sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            criar_cadastro(lista)     
        elif opcao == '2':
            lista_cadastros(lista)
        elif opcao == '3': 
            salvar_dados(lista)
            print("dados salvos com sucesso")
            break
        else: 
            print("Opção inválida tente novamente")


if __name__ == "__main__":
    menu()   
