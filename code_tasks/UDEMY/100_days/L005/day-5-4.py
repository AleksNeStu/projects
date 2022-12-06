#Write your code below this row 👇
is_divisible_by = lambda dig, divisors: all(
    [dig % div == 0 for div in divisors])
for num in range(1, 101):
    if is_divisible_by(num, [3, 5]):
        print('FizzBuzz')
    elif is_divisible_by(num, [5,]):
        print('Buzz')
    elif is_divisible_by(num, [3,]):
        print('Fizz')
    else:
        print(num)


#SOLUTION
##Write your code below this row 👇
#
# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)
#SOLUTION