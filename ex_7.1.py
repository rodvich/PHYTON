class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.my_list]))

    def __add__(self, other):
        for i in range(len(self.my_list)):
            for j in range(len(self.my_list[i])):
                self.my_list[i][j] += other.my_list[i][j]
        return Matrix(self.my_list)


first_list = [[12, 34, 56], [78, 90, 1]]
new_list = [[100, 1, 10], [1, 2, 3]]
matrix = Matrix(first_list)
my_matrix = Matrix(new_list)
print(my_matrix, '\n')
print(matrix, '\n')
print(matrix + my_matrix)
