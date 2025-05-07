import random

def gerar_username(nome, sobrenome, usar_simbolo=False):
    numeros = str(random.randint(10, 999))
    simbolos = ['_', '.', '-', '']
    simbolo = random.choice(simbolos) if usar_simbolo else ''
    
    username = f"{nome.lower()}{simbolo}{sobrenome.lower()}{numeros}"
    return username

# Exemplo de uso
print("=== Gerador de Nome de Usuário ===")
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
opcao = input("Deseja usar símbolo entre o nome e sobrenome? (s/n): ").lower()

usar_simbolo = opcao == 's'

for i in range(5):
    print(f"Username {i+1}: {gerar_username(nome, sobrenome, usar_simbolo)}")
