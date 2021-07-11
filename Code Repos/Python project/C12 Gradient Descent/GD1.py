import numpy as np


def grad(x):
    return 2 * x + 5 * np.cos(x)


def cost(x):
    return x * 2 + 5 * np.sin(x)

# eta: tốc độ học (learning rate)
def myGD1(x0, eta):
    x = [x0]
    for it in range(100):
       # EX: array([5, 0, 3, 3, 7, 9])
       # x1[-1] = 9 => the end of index
        x_new = x[-1] - eta * grad(x[-1]) #Xt+1 = Xt − ηf'(Xt) 
        # abs: trị tuyệt đối
        # nếu trị tuyệt đối của đạo hàm x_new đủ nhỏ
        if abs(grad(x_new)) < 1e-3: 
            break
        x.append(x_new)
    return (x, it)


(x1, it1) = myGD1(-5, .1)
(x2, it2) = myGD1(5, .1)
print("Solution x1 = %f, cost = %f, after %d iterations" %
      (x1[-1], cost(x1[-1]), it1))
print("Solution x2 = %f, cost = %f, after %d iterations" %
      (x2[-1], cost(x2[-1]), it2))
print("range(100): {}".format(range(100)))