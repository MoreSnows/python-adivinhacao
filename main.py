import random

print("Começou o jogo de adivinhação!")

# Constantes para as dificuldades
FACIL = 1
NORMAL = 2
DIFICIL = 3

# Mapeamento das dificuldades às quantidades de tentativas
dificuldades_tentativas = {FACIL: 20, NORMAL: 10, DIFICIL: 5}

# Pedir ao usuário escolher a dificuldade
dificuldade = int(input("Escolha a dificuldade (1) fácil (2) normal (3) difícil: "))

# Definir o número de tentativas com base na dificuldade escolhida
tentativas = dificuldades_tentativas[dificuldade]

# Número a ser adivinhado
numero = random.randint(1, 100)

for inicio in range(tentativas):
    # Informar ao usuário o número de tentativas restantes
    print("Você tem {} tentativas".format(tentativas))

    # Pedir o número para o usuário
    numero_advinhado = int(input("Digite um número de 1 a 100: "))

    # Verificar se o número foi adivinhado corretamente
    if numero_advinhado == numero:
        print("Parabéns! Você acertou o número", numero)
        break
    elif numero_advinhado <= 100:
        # Diminuir o número de tentativas
        tentativas -= 1

        # Fornecer dicas sobre se o número é maior ou menor que o número secreto
        if numero_advinhado > numero:
            print("O número é menor que", numero_advinhado)
        else:
            print("O número é maior que", numero_advinhado)

        # Verificar se o jogador não tem mais tentativas
        if tentativas == 0:
            print("Você perdeu! o numero era {}".format(numero))
            break
    else:
        continue
