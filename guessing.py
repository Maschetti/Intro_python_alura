import random

def game():
    print("*************************")
    print("Welcome to guessing game!")
    print("*************************")

    print("\n(1)Easy")
    print("(2)Medium")
    print("(3)Hard")
    nivel = int(input("Choose the dificulty: "))

    pontos = 100
    numero_secreto = random.randrange(1, 101)
    total_tentativas = 0

    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for tries in range (1, total_tentativas + 1, 1):
        print("Number of tries: {} of {}".format(tries, total_tentativas))
        chute = int(input("Guess a number between  1 and 100: "))
        acertou = numero_secreto == chute
        maior = chute > numero_secreto

        if(chute < 1 or chute > 100):
            print("Your guess must be lower than 100 and higher than 1")
            continue
    
        if(acertou):
            print("You guessed right! You scored {}".format(pontos))
            break
        elif(maior):
            print("You guessed wrong! The number is lower")
        else:
            print("You guessed wrong! The number is higher")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
        
    print("End Game!")
    
if(__name__ == "__main__"):
    game()