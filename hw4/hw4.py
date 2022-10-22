import numpy as np

if __name__ == "__main__":
    arr0 = np.zeros(10)
    arr1000_7 = np.array([i for i in range(1000, 0, -7)])
    arr_rand = np.random.rand(10)


def multiplication_check(list_of_matrix):
    a = np.shape(list_of_matrix[0])[0]
    b = np.shape(list_of_matrix[0])[1]
    for i in range(len(list_of_matrix)-1):
        if b != np.shape(list_of_matrix[i+1])[0]:
            return False
        else:
            b = np.shape(list_of_matrix[i+1])[1]
            a = np.shape(list_of_matrix[i])[0]
    return True



def matrix_multiplication(matrix1, matrix2):
    if multiplication_check([matrix1, matrix2]):
        return(np.dot(matrix1, matrix2))
    else:
        return None


def multiply_matrices(list_of_matrix):
    if multiplication_check(list_of_matrix):
        mat_res = list_of_matrix[0]
        for i in range(len(list_of_matrix)-1):
            mat_res = np.dot(mat_res, list_of_matrix[i+1])
        return mat_res
    else:
        return None


def compute_2d_distance(point_1, point_2):
    return np.sqrt(np.sum(np.square(point_1 - point_2)))


def compute_multidimensional_distance(point_1, point_2):
    return np.sqrt(np.sum(np.square(point_1 - point_2)))


def compute_pair_distances(matrix_coord):
    n = np.shape(matrix_coord)[0]
    mat_ans = np.zeros((n, n))
    for i in range(n):
        for j in range(i+1, n):
            mat_ans[i][j] = compute_multidimensional_distance(matrix_coord[i], matrix_coord[j])
            mat_ans[j][i] = mat_ans[i][j]
    return mat_ans

