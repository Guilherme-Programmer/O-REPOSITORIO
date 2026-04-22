import random

letra = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#"

tamanho_senha = int(input("Digite o tamanho da senha que quer gerar: "))

senha_gerada = ""

for i in range(tamanho_senha):
    senha_gerada = senha_gerada + random.choice(letra)
    
print(f"A senha gerada é: {senha_gerada}")