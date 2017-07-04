from sklearn import datasets

iris = datasets.load_iris()
digits = datasets.load_digits()

# test
digits
digits.target

print "test"

from sklearn import svm
clf = svm.SVC(gamma=0.001, C=100.)

clf.fit(digits.data[:-1],digits.target[:-1])


##########

x = [1,2,3,4]
y = [1,2,2,2]

import matplotlib.pyplot as plt
plt.scatter(x,y)
plt.show()