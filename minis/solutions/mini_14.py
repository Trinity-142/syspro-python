from random import randint
import matplotlib.pyplot as plt
import numpy as np

SIZE = 1024
ITER = 128
field = [[randint(0, 1) for x in range(SIZE)] for y in range(SIZE)]


def paint(a, str=""):
    fig, ax = plt.subplots()
    ax.imshow(a, cmap='binary', interpolation='nearest')
    plt.title('Game of Life ' + str)
    plt.draw()
    plt.pause(10**-100)

def neighbors(arr, row, col):
    sum_ = 0
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if (i == row and j == col) or (i < 0 or j < 0 or i >= SIZE or j >= SIZE):
                continue
            sum_ += arr[i][j]
    return sum_

def nextgen(prev_gen, next_gen):
    for i in range(SIZE):
        for j in range(SIZE):
            neighbor = neighbors(prev_gen, i, j)
            if (neighbor == 2 and prev_gen[i][j] == 1) or neighbor == 3:
                next_gen[i][j] = 1
            else:
                next_gen[i][j] = 0
    return next_gen


# -------------------
# списки
# -------------------

a = [i.copy() for i in field]
b = [[0] * SIZE for i in range(SIZE)]

paint(a)

for step in range(ITER):
    if step % 2 == 0:
        b = nextgen(a, b)
        current = b
    else:
        a = nextgen(b, a)
        current = a
    paint(current)
plt.pause(2)

# -------------------
# numpy array
# -------------------

a_np = np.array(field)
b_np = np.zeros((SIZE, SIZE))

paint(a_np, "numpy")

for step in range(ITER):
    if step % 2 == 0:
        b_np = nextgen(a_np, b_np)
        current_np = b_np
    else:
        a_np = nextgen(b_np, a_np)
        current_np = a_np
    paint(current_np, "numpy")

assert(np.array_equal(current_np, current_np))
plt.show()