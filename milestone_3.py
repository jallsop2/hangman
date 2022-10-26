import random

word_list = ['Apple','Banana','Orange','Pear','Grape']
word = random.choice(word_list)



def check_guess(word,guess):
    guess = guess.lower()
    if guess in word:
        print(f'Good guess! {guess} is in the word!')
    else:
        print(f'Sorry, {guess} is not in the word. Try again.')

def ask_for_input(word):
    while True:
        guess = input("Please enter your guess: ")

        if len(guess) == 1 and guess.isalpha() == True:
            break
        else:
            print('Invalid letter. Please enter a single alphabetical character.')
    
    check_guess(word,guess)

ask_for_input(word)