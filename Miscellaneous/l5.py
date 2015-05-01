# Restricted Boltzmans Machines (RBM) nets for digits classification
# It uses a pipeline and passes the RBM scores through that to a Logistic Regression classifier 

'''

SHORT NOTE ON RBM
Restricted boltzmann machines commonly known as ‘RBM’s are excellent feature extractors, working just like autoencoders. They easily outperform PCA (principal component analysis) and LDA when it comes to dimensionality reduction techniques. The features extracted from images (eg MNIST) are fed to neural networks or  machine learning algorithms such as SVM or Logistic regression classifiers. RBMs only work on inputs between 0 and 1 and even works very well on binary inputs. RBM are almost like NN except the rbm nodes are not connected to each other in the same layer.

'''

import numpy as np
from sklearn import datasets,metrics
from sklearn.neural_network import BernoulliRBM
from sklearn import linear_model
from sklearn.pipeline import Pipeline

#loading the data
digits = datasets.load_digits()
X = np.asarray(digits.data, 'float32') #(>>> X.shape = [1797,64])
X = (X - np.min(X, 0)) / (np.max(X, 0) + 0.0001)  # 0/1 scaling
Y=digits.target

#setting up the models
logistic = linear_model.LogisticRegression()
rbm = BernoulliRBM()


classifier = Pipeline(steps=[('rbm', rbm), ('logistic', logistic)])
logistic.C = 6000.0
rbm.n_iter = 30


# Training RBM-Logistic Pipeline
classifier.fit(X,Y)
Ypred=classifier.predict(X)

print 'accuracy'
print metrics.accuracy_score(Y,Ypred)

print 'Confusion Matrix'
print metrics.confusion_matrix(Y,Ypred)


'''
Obtained Output

accuracy : 0.996104618809
Confusion Matrix
[[178   0   0   0   0   0   0   0   0   0]
 [  0 181   0   0   0   0   0   0   1   0]
 [  0   0 177   0   0   0   0   0   0   0]
 [  0   0   0 181   0   1   0   0   1   0]
 [  0   0   0   0 181   0   0   0   0   0]
 [  0   0   0   0   0 181   0   0   0   1]
 [  0   0   0   0   0   0 181   0   0   0]
 [  0   0   0   0   0   0   0 179   0   0]
 [  0   0   0   0   0   0   0   0 173   1]
 [  0   0   0   1   0   0   0   0   1 178]]

'''
