# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

# Milestone 2 
First I used VScode to create a python file and initialised a list of fruits.
Then I imported the random package and used the random.choose() function to let the computer choose a word from the list for the game.
Then I used the input function to take a letter guess from the player and checked whether it was a valid guess with an if statement and the isalpha function.

```python
import random

word_list = ['Apple','Banana','Orange','Pear','Grape']
word = random.choice(word_list)

alphabet = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']

guess = input("Please enter your guess: ")

if len(guess) == 1 and guess.isalpha() == True:
    print('Good Guess!')
else:
    print('Oops! That is not a valid input.')
```

![Output](Milestone_2_output.png)

# Milestone 3
I created functions to accept a guess from the player and check it is valid, and also to check whether it is in the word created in milestone 2.

```python
def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f'Good guess! {guess} is in the word!')
    else:
        print(f'Sorry, {guess} is not in the word. Try again.')

def ask_for_input():
    while True:
        guess = input("Please enter your guess: ")

        if len(guess) == 1 and guess.isalpha() == True:
            break
        else:
            print('Invalid letter. Please enter a single alphabetical character.')
    
    check_guess(guess)
```
![Output](Milestone_3_output.png)

# Milestone 4

I created a hangman class to control the game state, and included the functions from milestone 3 as methods. It also has attributes for the word, what the player has guessed, the number of letters left, the list of guessses and the number of lives.

```python
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
            for i in range(0,len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
            
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word.')
            print(f'You have {self.num_lives} lives left.')

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
```

# Milestone 5

I finished the game by creating a function which plays the game. Inside it runs a while loop which checks if the player has won or lost the game with the num_lives and num_letters attributes, and then continues the game with the ask_for_input method if not.

```python

def play_game(word_list):
    number_of_lives = 5
    game = Hangman(word_list,number_of_lives)
    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        
        if game.num_letters == 0:
            print('Congratulations. You won the game!')
            break

        game.ask_for_input()
```