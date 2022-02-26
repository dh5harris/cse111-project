# this is the final project for CSE111 "Programming with Functions" class at BYU-Idaho for the Fall '21 semester
# import the random module to pick a random word from the word_list.
import random


def main():
    word = get_word()
    play_game(word)

    # A while loop to see if the user wants to keep playing.
    while input('Play again (Y/N)? ').upper() == 'Y':
        word = get_word()
        play_game(word)
    else:
        print('Thanks for playing!')


def get_word():
    """Return a randomly choosen word from the list 'words'.
    Return: a randomly choosen word."""

    words = ['adult', 'animal', 'ate', 'bird', 'basket', 'because', 'book', 'card', 'cat', 'child', 'cloud', 'debt', 
    'desire', 'drank', 'door', 'earth', 'father', 'finger', 'free', 'girl', 'green', 'grew', 'man', 'woman', 'happy', 
    'hearing', 'history', 'horse', 'interest', 'knife','laughed', 'library', 'love', 'manager', 'married',  
    'thought','opinion', 'opposite', 'ran', 'payment','peekaboo', 'reason', 'religion', 'phone', 
    'science','slept', 'sneeze', 'talked', 'walked', 'wrote', 
    'abruptly', 'absurd', 'affix', 'avenue', 'awkward','banjo', 'beekeeper', 'blizzard', 'boggle', 
    'buzzard', 'cobweb', 'croquet', 'cycle', 'disavow', 'dizzying', 'duplex', 'embezzle', 'exodus', 'faking', 
    'flapjack', 'flopping', 'fluffiness', 'frazzled', 'fuchsia','gabby', 'galaxy', 'gizmo', 'gnarly', 
    'hyphen', 'icebox', 'injury', 'jackpot', 'jinx', 'joyful', 'juicy', 'jukebox', 'jumbo', 
    'kayak','kilobyte', 'kiosk', 'knapsack', 'luxury', 'lymph', 'matrix', 'megahertz', 'microwave', 'mystify', 
    'nowadays', 'oxygen', 'phlegm', 'pixel', 'pneumonia', 'polka', 'puzzling', 'quartz', 'quorum', 
    'rhythm', 'scratch', 'strength', 'stretch', 'stronghold', 'subway', 'thriftless', 'transcript',
    'unknown','uptown', 'vaporize', 'vortex', 'whomever', 'wimpy', 'wizard', 'woozy', 'wristwatch', 
    'xylophone', 'yoked', 'youthful', 'yummy', 'zipper', 'zodiac', 'zombie']

    # Randomly chooses and returns a word in all uppercase. 
    word = random.choice(words)
    return word.upper()

def play_game(word):
    """ The play game fuction of the hangman game. Displays the word to be guessed as underscores.
        Displays the gallows. As letters are correctly guessed, replace underscores with letters.
    Parameter 
        word: The secert word to be guessed by the user.
    Return: nothing"""

    # The unguessed word will be shown as underscores. 
    word_to_guess = '_' * len(word)
    # There will be six wrong attempts to figure out the word.
    attempts = 6
    # For the word has not been guessed correctly or solved.
    guessed = False
    # The guessed letters will be stored in list called guessed_letters.
    guessed_letters = []

    # Print the welcome to Hangman.
    print('Welcome to Hangman!')
    # Print how many characters the word has.
    print(f'The word is {len(word)} letters long.')
    # Print the gallows.
    print(display_hangman(attempts))
    # Print the word that is to be guessed. Unscores for each letter.
    print(word_to_guess)
    # Print a blank line.
    print()

    # A while loop for while the word has not been guessed and the wrong attempts is greater that zero.
    while not guessed and attempts > 0:
        # Print out the number of attempts that user has left.
        print(f'You have {attempts} wrong guesses remaing.')
        # The user guesses a letter.
        guess = get_guess('Please guess a letter. ')
        # Check if the guessed letter has been guessed before 
        # and is the guessed_letters list.
        if guess in guessed_letters:
            # Print out that the letter was already guessed.
            print(f'Oops. You already guessed {guess}')
            print(f'You have used: {guessed_letters}')

        # Check if the guessed letter is not been guessed before.
        elif guess not in word:
            print(f'Nope. {guess}, is not in the word.')
            # Subtract 1 from the attempts when the guess is wrong.
            attempts -= 1
            # Add the letter to the guessed_letters list.
            guessed_letters.append(guess)
            # Print out the letters that have already been guessed.
            print(f'You have used: {guessed_letters}')

        # When the guessed letter is in the word.    
        else:
            # Print the letter that is in the word.
            print(f'Good Guess. {guess} is in the word.')
            # Added the guessed letter to the guessed_letter list.
            guessed_letters.append(guess)
            # This to take the word that is to be guessed and to split it into single letters.
            word_as_list = list(word_to_guess)
            indices = [i for i, letter in enumerate(word) if letter == guess]
            for index in indices:
                word_as_list[index] = guess
            # This is to bring the single letters back into the word.
            word_to_guess = "".join(word_as_list)
            # When there is no more "_" in the word_to_guess variable, the word has been guessed correctly.
            if "_" not in word_to_guess:
                guessed = True
            # Print what letters have been used so far.
            print(f'You have used: {guessed_letters}')
        # Print the gallows for the various stages.
        print(display_hangman(attempts))
        # Print underscores for letters not guessed and the letters that have been guessed.
        print(word_to_guess)
        # Print a blank line.
        print()

    # Print the congratulations when the word has been guessed correctly.
    if guessed:
        print(f'Congrats, you guess the word.')
        print('You win!')
        print()

    # Print the message that the user ran out of attempts and revile the secert word.
    else:
        print(f'Sorry, you ran out of tries.')
        print(f'The word was {word}.')
        print()


def get_guess(prompt):
    """Get the user input for the letter they are gussing.
        Parameter
            prompt: The prompt displayed, for the input statment, to the user to get thier guess.
        Return: The letter the user guessed"""
    # A while loop for if the user enter a wrong character or too many letters or characters
    while True:
        
        guess = input(prompt).upper()
        if len(guess) != 1:
            print('You entered to many letters.')
            # guess = input(f'Please enter a single letter. ').upper()
        elif guess not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            print('That is not a letter.')
            # guess = input(f'Please enter a LETTER. ').upper()
        else:
            # Return the users guess
            return guess
        


def display_hangman(attempts):
    """Print the gallows for the hangman game for the various stages of the game.
    Parameter 
        attempts: The number of wrong attempts the user has or has left
        in the game.
    Return: the coresponding index of the list with the attempts that are remaining.
        If the user has five attempts left, the image of the fifth index postion 
        is returned.  """
    gallows = [
        """
            ------
            |    |
            |    O
            |   \|/
            |    |
            |   / \\
            |
        ____|________""",
        """
            ------
            |    |
            |    O
            |   \|/
            |    |
            |   / 
            |
        ____|________""",
        """
            ------
            |    |
            |    O
            |   \|/
            |    
            |   
            |
        ____|________""",
        """
            ------
            |    |
            |    O
            |   \|
            |    
            |   
            |
        ____|________""",
        """
            ------
            |    |
            |    O
            |    |
            |    
            |   
            |
        ____|________""",
        """
            ------
            |    |
            |    O
            |    
            |    
            |   
            |
        ____|________""",
        """
            ------
            |    |
            |    
            |    
            |    
            |   
            |
        ____|________""",
    ]
    # Return the image of the gallows from the corresponding attempt.
    return gallows[attempts]

# Call the main function to start this program
if __name__ == "__main__":
    main()