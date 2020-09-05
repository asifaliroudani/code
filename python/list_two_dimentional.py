matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0])
print(matrix[0][1])

for row in matrix:
    for items in row:
        print(items)

flatten_list = []
for row in matrix:
    for items in row:
        flatten_list.append(items)
print(flatten_list)