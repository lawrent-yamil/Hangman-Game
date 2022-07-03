#Import libraries
import random

palabras = ["hola", "mundo", "python", "programacion", "coding", "hangman", "chocolate",]

class Game():
    def __init__(self):
        self.word = random.choice(palabras)
        self.guesses = []
        self.lives = 6

    def guess(self, letter):
        if letter in self.word:
            self.guesses.append(letter)
        else:
            self.lives -= 1

    def display(self):
        for letter in self.word:
            if letter in self.guesses:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print()

    def won(self):
        for letter in self.word:
            if letter not in self.guesses:
                return False
        return True

    def lost(self):
        if self.lives == 0:
            return True
        return False

    def play(self):
        while not self.lost() and not self.won():
            self.display()
            print("Tu tienes {} vidas restantes.".format(self.lives))
            guess = input("Adivina una letra: ")
            self.guess(guess)
        if self.lost():
            print("¡Has perdido!")
        elif self.won():
            print("¡Has ganado!")
        print("La palabra era {}.".format(self.word))


if __name__ == "__main__":
    game = Game()
    game.play()