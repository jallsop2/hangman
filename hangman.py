import random
import english_words

word_list = list(english_words.english_words_lower_set)


class Hangman():
    def __init__(self,word_list):
        
        while True:
            self.word = random.choice(word_list).upper()
            if self.word.isalpha() == False or len(self.word) <= 3:
                continue
            break

        self.word_guessed = ['_']*len(self.word)
        
        self.num_letters = len(list(set(self.word)))
        
        self.num_lives = 5

        self.word_list = word_list

        self.list_of_guesses = []

    def check_guess(self,guess):
        if guess in self.word:
            print(f'\nGood guess! {guess} is in the word.')
            for i in range(0,len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
            
        else:
            self.num_lives -= 1
            print(f'\nSorry, {guess} is not in the word.')

    def ask_for_input(self):
        while True:
            print()
            for i in self.word_guessed:
                print(i, end = "")

            if self.num_lives < 5:
                print('\n \nThe incorrect letters guessed are:')
                for i in self.list_of_guesses:
                    if i not in self.word:
                        print(i, end = ' ')

            print(f'\n \nYou have {self.num_lives} lives left.')

            guess = input("\nPlease enter your guess: ").upper()

            if guess == 'stop':
                return 1

            if len(guess) != 1 or guess.isalpha() == False:
                print('\nInvalid guess. Please enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('\nYou already guessed that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess) 
                break



def play_game(word_list):

    game = Hangman(word_list)
    while True:
        if game.num_lives == 0:
            print(f'\nYou lost! The word was {game.word}.')
            break
        
        if game.num_letters == 0:
            print(f'\nCongratulations, the word was {game.word}. You won the game!')
            break

        switch = game.ask_for_input()

        if switch == 1:
            break

play_game(word_list)