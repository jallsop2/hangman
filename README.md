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