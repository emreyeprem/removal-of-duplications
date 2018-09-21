# Python 3.x code to demonstrate star pattern
# Function to demonstrate printing pattern
# def pypart(n):
#
#     # outer loop to handle number of rows
#     # n in this case
#     for i in range(0, n):
#
#         # inner loop to handle number of columns
#         # values changing acc. to outer loop
#         for j in range(0, i+1):
#
#             # printing stars
#             print("* ",end="")
#
#         # ending line after each row
#         print("\r")
# pypart(n)

#Second try:
# for i in range(0, 7):
#     for j in range(0, i+1):
#         print("* ",end="")
#     print()

#third try

# k = 0
# rows = 8
# for i in range(1, rows+1):
#     for space in range(1, (rows-i)+1):
#         print(end="  ")
#     while k != (2*i-1):
#         print("* ", end="")
#         k = k + 1
#     k = 0
#     print()

# Final try (assignment)
character = '*'
for i in range(1,18,2):
    print("{:^45}".format(character * i))
