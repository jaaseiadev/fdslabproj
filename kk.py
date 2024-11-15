import numpy as np
import matplotlib.pyplot as plt

C = 100
D = 0.1
dt = 1
dx = 1

matrix_size = 100
matrix = np.zeros((matrix_size, matrix_size))
matrix[50, 50] = C

im = plt.imshow(matrix, cmap="viridis")
plt.colorbar(im)
plt.show()

for t in range(0, 1000):
    new_matrix = matrix.copy()
    for x in range(1, matrix_size - 1):
        for y in range(1, matrix_size - 1):
            new_matrix[x, y] = (
                    matrix[x, y]
                    + ((D * dt) / (dx ** 2)) * (matrix[x + 1, y] - 2 * matrix[x, y] + matrix[x - 1, y])
                    + ((D * dt) / (dx ** 2)) * (matrix[x, y + 1] - 2 * matrix[x, y] + matrix[x, y - 1])
            )
    matrix = new_matrix

    if t % 100 == 0:
        plt.title(f"TIME = {t}")
        im = plt.imshow(matrix, cmap="viridis")
        plt.colorbar(im)
        plt.show()
