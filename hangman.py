"""Hangman game"""

from secrets import choice

# words to guess
dictionary = ['wword', 'wowrld', 'wwwpuzzle']

# Picks a random word to guess
picked_word = choice(dictionary)

# cheat
print(picked_word)

# Print user 'GUI' :D, len by picked word
user_gui = ['_' for char in picked_word]

print(' '.join(user_gui))

life_left = len(picked_word)

while life_left > 0:
    # User guessing a letter
    guessed_letter = input('Guess a letter: ').lower()

    # Find and storing all indexes of a guessed letter
    indexes = []

    for i, c in enumerate(picked_word):
        if c == guessed_letter:
            indexes.append(i)
            user_gui[i] = guessed_letter

    print(f"Found guessed letters '{guessed_letter}' at indexes {indexes}")
    # print(list(user_gui))
    print(' '.join(user_gui))



# # Check for an answer
# if guessed_letter in picked_word:
#     print(
#         f'guessed letter {guessed_letter} is used {picked_word.count(guessed_letter)} times.'
#     )
# else:
#     print('Guessed wrong.')
