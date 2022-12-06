# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
# first, second = list(map(int, list(position)))
# elem_idx, row_idx = list(map(int, list(position)))
elem_idx, row_idx = [int(digit) - 1 for digit in list(position)]
map[row_idx][elem_idx] = "X"
#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

#SOLUTION
# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
#
# position = input("Where do you want to put the treasure? ")
#
# horizontal = int(position[0])
# vertical = int(position[1])
#
# map[vertical - 1][horizontal - 1] = "X"
#
# print(f"{row1}\n{row2}\n{row3}")
#SOLUTION