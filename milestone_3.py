
while True:
    guess = input("Please enter your guess: ")

    if len(guess) == 1 and guess.isalpha() == True:
     break
    else:
        print('Invalid letter. Please enter a single alphabetical character.')