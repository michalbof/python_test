"""Loops"""

# student_heights = [180, 124, 165, 173, 189, 169, 146]

# suma:int = 0
# loop_round:int = 0

# for i in student_height:
#     suma += i
# print(suma)

# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)

# loopn: int = 0
# total_height: int = 0
# for i in student_heights:
#     total_height += i
#     loopn += 1
# print(round(total_height / loopn))

# # Finding a max value in a list

# in_values = input('Input random values: ').split()
# in_values = map(int, in_values)
# max_val: int = 0

# for value in in_values:
#     if value > max_val:
#         max_val = value
# print(max_val)

# # Testing how range works

# old:int = 0
# for number in range(1, 101):
#     old += number
# print(old)

# # Print sum of all the even numbers from 1 to 100 included

# total: int = 0
# for number in range(1, 101):
#     if number % 2 == 0:
#         total += number
# print(total)

# total2: int = 0
# for number in range(2, 101, 2):
#     total2 += number
# print(total2)

# # Fizz Buzz - if divisible by 3 'Fizz' if by 5 'Buzz' and if by both 'FizzBuzz"

# for num in range(1,101):
#     if num % 3 and num % 5 == 0:
#         print('FizzBuzz')
#     elif num % 3 == 0:
#         print('Fizz')
#     elif num % 5 == 0:
#         print('Buzz')
#     else:
#         print(num)
