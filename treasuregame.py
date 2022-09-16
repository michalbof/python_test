"""Treasure game"""
row1 = ['11', '12', '13']
row2 = ['21', '22', '23']
row3 = ['31', '32', '33']

map_list = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

user_input = input('Pick coordinates:')
# user_input_coordinates = [*user_input]

# first_number = int(user_input_coordinates[0])
# second_number = int(user_input_coordinates[1])

first_number = int(user_input[0])
second_number = int(user_input[1])

map_list[first_number-1][second_number-1] = 'x'

print(f"{row1}\n{row2}\n{row3}")
