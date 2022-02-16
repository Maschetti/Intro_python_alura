import guessing
import hangman

print("**************************")
print("*****Choose one game!*****")
print("**************************")

print("(1)Hangman game\n(2)Guessing game")
jogo = int(input("Your choice: "))

if(jogo == 1):
    hangman.game()
else:
    guessing.game()
