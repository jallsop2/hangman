import random

word_list = ['apple','banana','orange','pear','grape']
word = random.choice(word_list)

class Hangman():
    def __init__(self,word_list,num_lives = 5):
        self.word = random.choice(word_list)
        print(self.word)

        self.word_guessed = ['_']*len(self.word)
        
        self.num_letters = len(list(set(self.word)))
        
        self.num_lives = num_lives

        self.word_list = word_list

        self.list_of_guesses = []

    def check_guess(self,guess):
        guess = guess.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
        else:
            print(f'Sorry, {guess} is not in the word. Try again.')

    def ask_for_input(self):
        while True:
            guess = input("Please enter your guess: ")

            if len(guess) != 1 or guess.isalpha() == False:
                print('Invalid letter. Please enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess) 
                break
                
game = Hangman(word_list)
game.ask_for_input()