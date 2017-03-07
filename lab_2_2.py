from sklearn import svm
from matplotlib import pyplot as plt

#wczytanie danych z pliku
def load_data(filename):
    X = []
    for line in open(filename):
        tokens = line.split()
        X.append([float(tokens[0]),float(tokens[1]),float(tokens[2])])
    return(X)

#klasyfikacja dancyh
def classify(X):
    Xs = []
    ys = []
    for [x,y,c] in X:
        if c == 1 or c == 0:
            Xs.append([x,y])
            ys.append(c)
    clf = svm.SVC()
    clf.fit(Xs,ys)
    for i in range(len(X)):
        if X[i][2] == -1:
            X[i][2] = clf.predict([X[i][0],X[i][1]])
    return X

    # klasyfikator = svm.SVC()
    # X = [[2,1],[3,4],[5,7]]
    # c = [1,0,1]
    # klasyfikator.fit(X,c)
    # print(klasyfikator.predict([3,2]))

def draw_data(X):
    xs1 = []
    ys1 = []
    xs0 = []
    ys0 = []
    xsn = []
    ysn = []
    for [x, y, c] in X:
        if c == 1:
            xs1.append(x)
            ys1.append(y)
        if c == 0:
            xs0.append(x)
            ys0.append(y)
        if c == -1:
            xsn.append(x)
            ysn.append(y)

    plt.axis([-5,15,-5,15])
    plt.plot(xsn, ysn, 'ro', color='black')
    plt.plot(xs0, ys0, 'ro', color='red')
    plt.plot(xs1, ys1, 'ro', color='blue')

    plt.show()

draw_data(load_data('train'))

draw_data(classify(load_data('train')))

