from typing import List


class Matrix:
    def __init__(self, list_of_lists: List[List[float]]) -> None:
        self.grid = list_of_lists

    def get_sub_matrix(self, quadrant):
        # Top left = 1
        # Top right = 2
        # Bottom left = 3
        # Bottom right = 4
        length_sub = len(self.grid[0]) // 2
        depth_sub = len(self.grid) // 2
        if quadrant == 1:
            return Matrix([arr[:length_sub] for arr in self.grid[:depth_sub]])
        elif quadrant == 2:
            return Matrix([arr[length_sub:] for arr in self.grid[:depth_sub]])
        elif quadrant == 3:
            return Matrix([arr[:length_sub] for arr in self.grid[depth_sub:]])
        return Matrix([arr[length_sub:] for arr in self.grid[depth_sub:]])

    def __add__(self, matrix):
        new = []

        for y in range(len(self.grid)):
            row = []
            for x in range(len(self.grid[0])):
                row.append(self.grid[y][x] + matrix.grid[y][x])
            new.append(row)

        return Matrix(new)

    def __mul__(self, const):
        new = []

        for y in range(len(self.grid)):
            row = []
            for x in range(len(self.grid[0])):
                row.append(self.grid[y][x]*const)
            new.append(row)

        return Matrix(new)


def combine_sub_matrices(Q1: Matrix, Q2: Matrix, Q3: Matrix, Q4: Matrix):
    q1 = Q1.grid
    q2 = Q2.grid
    q3 = Q3.grid
    q4 = Q4.grid

    # merge q1 and q2
    q1_and_q2 = []
    for x in range(len(q1)):
        q1_and_q2.append([num for num in q1[x]]+[num for num in q2[x]])

    q3_and_q4 = []
    for x in range(len(q3)):
        q3_and_q4.append([num for num in q3[x]]+[num for num in q4[x]])

    return Matrix(q1_and_q2+q3_and_q4)


def strassen(x: Matrix, y: Matrix):
    X = x.grid
    Y = y.grid
    if len(X) == 1 and len(X[0]) == 1:
        return Matrix([[X[0][0]*Y[0][0]]])

    A = x.get_sub_matrix(1)
    B = x.get_sub_matrix(2)
    C = x.get_sub_matrix(3)
    D = x.get_sub_matrix(4)
    E = y.get_sub_matrix(1)
    F = y.get_sub_matrix(2)
    G = y.get_sub_matrix(3)
    H = y.get_sub_matrix(4)

    P1 = strassen(A, F+(H*(-1)))
    P2 = strassen(A+B, H)
    P3 = strassen(C+D, E)
    P4 = strassen(D, G+(E*(-1)))
    P5 = strassen(A+D, E+H)
    P6 = strassen(B+(D*(-1)), G+H)
    P7 = strassen(A+(C*(-1)), E+F)

    return combine_sub_matrices(P5+P4+(P2*(-1))+P6, P1+P2, P3+P4, P1+P5+((P3+P7)*(-1)))


m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6], [7, 8]])

print(strassen(m1, m2).grid)
