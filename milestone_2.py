import random

word_list = ['Apple','Banana','Orange','Pear','Grape']
word = random.choice(word_list)

alphabet = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']

guess = input("Please enter your guess: ")

if len(guess) == 1 and guess in alphabet:
    print('Good Guess!')
else:
    print('Oops! That is not a valid input.')