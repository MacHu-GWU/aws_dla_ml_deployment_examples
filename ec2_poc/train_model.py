# -*- coding: utf-8 -*-

"""
Reference:

https://scikit-learn.org/stable/auto_examples/classification/plot_classification_probability.html#sphx-glr-auto-examples-classification-plot-classification-probability-py
"""

import numpy as np

from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.gaussian_process.kernels import RBF
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data[:, 0:2]  # we only take the first two features for visualization
y = iris.target

n_features = X.shape[1]

C = 10
kernel = 1.0 * RBF([1.0, 1.0])  # for GPC

classifier = LogisticRegression(
    C=C, penalty="l1", solver="saga", multi_class="multinomial", max_iter=10000
)

classifier.fit(X, y)

y_pred = classifier.predict(X)
print(X)
print(y_pred)
