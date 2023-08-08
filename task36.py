import os
os.system('cls')
def print_operation_table(operation, num_rows=6, num_columns=6):

    print(" ".join(str(i) for i in range(1, num_columns + 1)))

    for row in range(1, num_rows + 1):
        row_values = [operation(row, col) for col in range(1, num_columns + 1)]
        print(" ".join(str(value) for value in row_values))

print_operation_table(lambda x, y: x * y)

