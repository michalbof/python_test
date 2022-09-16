'''random intro'''
import random

# random_int = random.randint(1, 2)
# print(random_int)

# rand_float = random.random() * 5
# print(rand_float)

# if random_int == 1:
#     print('heads')
# else:
#     print('tails')

random_words = ['This', 'ensures ', 'that ', 'we ', 'need ', 'to ', 'be ', 'mindful ',
                'of ', 'our ', 'seed', ' when']

# print(random.choice(random_words))
# random_words.append('!')
# print(random_words[-1])
# print(len(random_words))

# Waiting for user input
list_of_names = input("Give me names to choose from: ")

# creates a list from provided names
choose_rnd_name = list_of_names.split(", ")

# chooses random person from list
chosen_person = random.randint(0, len(choose_rnd_name)-1)

# who is buing today?
print(f"{choose_rnd_name[chosen_person]} is buing today's lunch.")
