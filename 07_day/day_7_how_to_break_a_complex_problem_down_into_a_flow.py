# LINK: https://ascii.co.uk/art

import random
import hangman_art
import hangman_words

print(f"{hangman_art.logo}")

chosen_word = random.choice(hangman_words.word_list)

lives = 6

print(f'Pssst, the solution is {chosen_word}.')
count = 0
display = []
word_length = len(chosen_word)

#while display != chosen_word:
for _ in range(word_length):
    display += "_"
    count += 1
print(display)
print(f"The word have {count} letters.")

end_game = False

while not end_game:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\nCurrent letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_game = True
            print("You lose!!!")

    print(f"{' '.join(display)}")
    
    if "_" not in display:
        end_game = True
        print("You win!!!")
    
    print(f"{hangman_art.stages[lives]}")
            