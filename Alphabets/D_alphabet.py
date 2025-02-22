x = 5
for i in range(x):
    for j in range(x):
        if j == 0 or (i == 0 and j < x - 1) or (i == x - 1 and j < x - 1) or (j == x - 1 and i != 0 and i != x - 1):
            print("*", end="")
        else:
            print(" ", end="")
    print()



# x = 5  # x of the square

# for i in range(x):
#     for j in range(x):
#         if (i == 0 or i == x - 1 or j == 0 or j == x - 1) and not ((i == 0 and j == x - 1) or (i == x - 1 and j == x - 1)):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()