import random
numero_apostado = 0
opcao = ""
bicho_sorteado = None
# Dicionário dos bichos e seus números correspondentes
bichos = {
"Avestruz":     [1, 2, 3, 4],
    "Águia":    [5, 6, 7, 8],
    "Burro":    [9, 10, 11, 12],
    "Borboleta":[13, 14, 15, 16],
    "Cachorro": [17, 18, 19, 20],
    "Cabra":    [21, 22, 23, 24],
    "Carneiro": [25, 26, 27, 28],
    "Camelo":   [29, 30, 31, 32],
    "Cobra":    [33, 34, 35, 36],
    "Coelho":   [37, 38, 39, 40],
    "Cavalo":   [41, 42, 43, 44],
    "Elefante": [45, 46, 47, 48],
    "Galo":     [49, 50, 51, 52],
    "Gato":     [53, 54, 55, 56],
    "Jacaré":   [57, 58, 59, 60],
    "Leão":     [61, 62, 63, 64],
    "Macaco":   [65, 66, 67, 68],
    "Porco":    [69, 70, 71, 72],
    "Pavão":    [73, 74, 75, 76],
    "Peru":     [77, 78, 79, 80],
    "Touro":    [81, 82, 83, 84],
    "Tigre":    [85, 86, 87, 88],
    "Urso":     [89, 90, 91, 92],
    "Veado":    [93, 94, 95, 96],
    "Vaca":     [97, 98, 99, 0]
}

# Exibe a tabela dos bichos
print("\n🐾 Lista dos bichos no Jogo do Bicho 🐾")
for numero, nome in bichos.items():
    print(f"{numero}: {nome}")

# Entrada do usuários 
while True:
    opcao = input("Na cabeça ou milhar? ")
    if opcao == "sair":
        print("🎲 Jogo encerrado! Obrigado por jogar.")
        break
    
    # JOGAR NO BIXO APENAS
    if opcao == "cabeça":
        num_cabeca = int(input("\nEscolha o número do bicho para apostar (0-99): "))
        valor_aposta = float(input("Digite o valor da aposta (R$): "))
        num_sorteado = random.randint(0, 99)
        for bicho, numeros in bichos.items():
            if num_sorteado in numeros:
                bicho_sorteado = bicho
                break
        print(f"\n🎲 Número sorteado: {num_sorteado} - {bicho_sorteado}")
        if num_cabeca == num_sorteado:
            premio = valor_aposta * 15  # Multiplicador fictício
            print(f"🎉 Parabéns! Você ganhou R$ {premio:.2f}!")
        else:
            print("😢 Você perdeu. Tente novamente!")
            
    
    # JOGAR NA MILHAR APENAS
    if opcao == "milhar":
        num_milhar = int(input('Digite o seu milhar:'))
        valor_aposta = float(input("Digite o valor da aposta (R$): "))
        num_sorteado = random.randint(1000, 9999)
        ultimos_dois = num_sorteado % 100 
       
        for bicho, numeros in bichos.items():
            if ultimos_dois in numeros:
                bicho_sorteado = bicho
                break  # Para a busca assim que encontrar
        print(f"\n🎲 Número sorteado: {num_sorteado} - {bicho_sorteado}")

        # Verifica se ganhou
        if num_milhar == num_sorteado:
            premio = valor_aposta * 18  # Multiplicador fictício
            print(f"🎉 Parabéns! Você ganhou R$ {premio:.2f}!")
        else:
            print("😢 Você perdeu. Tente novamente!")

    

   



