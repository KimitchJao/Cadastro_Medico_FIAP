import json
import os

# Nome do arquivo JSON que será usado como banco de dados
database_file = 'cadastro_medico.json'

def criar_arquivo_json():
    if not os.path.exists(database_file):
        dados = {
            'medicos': [],
            'procedimentos': []
        }
        with open(database_file, 'w') as file:
            json.dump(dados, file, indent=2)

def carregar_dados():
    criar_arquivo_json()
    
    try:
        with open(database_file, 'r') as file:
            dados = json.load(file)
    except FileNotFoundError:
        dados = {
            'medicos': [],
            'procedimentos': []
        }
    return dados

def salvar_dados(dados):
    with open(database_file, 'w') as file:
        json.dump(dados, file, indent=2)

def confirmar_limpeza():
    confirmacao = input("Tem certeza que deseja limpar o console? (S/N): ").lower()
    return confirmacao == 's'

def limpar_tela(exibir_lista=True):
    if confirmar_limpeza():
        sistema = os.name
        if sistema == 'nt':  # Windows
            os.system('cls')
        else:
            os.system('clear')  # Linux/MacOS

    if exibir_lista:
        print("\n=== Sistema de Cadastro Médico Unificado ===")

def limpar_historico():
    if confirmar_limpeza():
        dados = {
            'medicos': [],
            'procedimentos': []
        }
        salvar_dados(dados)
        print("Histórico limpo com sucesso.")
    else:
        print("Operação cancelada.")

def cadastrar_medico(nome, ocupacao):
    dados = carregar_dados()
    medico = {'nome': nome, 'ocupacao': ocupacao, 'procedimentos': []}
    dados['medicos'].append(medico)
    salvar_dados(dados)

def cadastrar_procedimento(medico_idx, procedimento, estado):
    dados = carregar_dados()
    
    if 0 <= medico_idx < len(dados['medicos']):
        procedimento_info = {'procedimento': procedimento, 'estado': estado}
        dados['medicos'][medico_idx]['procedimentos'].append(procedimento_info)
        salvar_dados(dados)
    else:
        print('Médico não encontrado.')

def listar_medicos():
    dados = carregar_dados()
    for i, medico in enumerate(dados['medicos']):
        print(f"{i + 1}. Nome: {medico['nome']}, Ocupação: {medico['ocupacao']}")
        print("   Procedimentos Realizados:")
        for procedimento in medico['procedimentos']:
            print(f"      - {procedimento['procedimento']} ({procedimento['estado']})")
        print()

def main():
    while True:
        limpar_tela(exibir_lista=False)  # Limpa a tela no início do loop, sem exibir a lista
        print("""=== Sistema de Cadastro Médico Unificado ===
        
1. Cadastrar Médico
2. Cadastrar Procedimento
3. Listar Médicos
4. Limpar Histórico
0. Sair""")

        escolha = input("\nEscolha a opção: ")

        if escolha == '1':
            nome = input("Digite o nome do médico: ")
            ocupacao = input("Digite a ocupação do médico: ")
            cadastrar_medico(nome, ocupacao)
        elif escolha == '2':
            listar_medicos()
            medico_idx = int(input("Digite o número do médico para cadastrar o procedimento: ")) - 1
            procedimento = input("Digite o procedimento realizado: ")
            estado = input("Digite o estado onde o procedimento foi realizado: ")
            cadastrar_procedimento(medico_idx, procedimento, estado)
        elif escolha == '3':
            limpar_tela()  # Limpa a tela antes de exibir a lista
            listar_medicos()
        elif escolha == '4':
            limpar_historico()
        elif escolha == '0':
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
