from sklearn.linear_model import LinearRegression
import numpy as np

X= np.random.rand(1000);
y = 4 + 3 * X + .5*np.random.randn(1000) # noise added
a = np.arange(2,10)
#y = 4 + 3 * a + .5*a
#print("y: {}".format(y)) 
# print("a.reshape((-1,1)) : {}".format(a.reshape((-1,1)))) 
# (-1,1) ở đây có nghĩa là chỉ cần cột là 1 còn bao nhiêu hàng thì tùy theo có bao nhiêu giá trị
# model = LinearRegression()
# model.fit(X.reshape(-1,1), y.reshape(-1,1))
# w, b = model.coef_[0][0], model.intercept_[0]
# sol_sklearn = np.array([b, w])
# print(sol_sklearn)
one = np.ones((X.shape[0], 1))
Xbar = np.concatenate((one, X), axis = 1) # each point is one row
def grad(w):
    N=Xbar.shape[0]
    return 1/N * Xbar.T.dot(Xbar.dot(w) - y)
X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T
