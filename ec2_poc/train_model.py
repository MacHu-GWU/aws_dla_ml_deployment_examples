# -*- coding: utf-8 -*-

"""
Reference:

https://scikit-learn.org/stable/auto_examples/classification/plot_classification_probability.html#sphx-glr-auto-examples-classification-plot-classification-probability-py
"""

import os
import pickle
import numpy as np

from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.gaussian_process.kernels import RBF
from sklearn import datasets


def train_model():
    iris = datasets.load_iris()
    X = iris.data[:, 0:2]  # we only take the first two features for visualization
    y = iris.target

    C = 10

    classifier = LogisticRegression(
        C=C, penalty="l1", solver="saga", multi_class="multinomial", max_iter=10000
    )

    classifier.fit(X, y)

    return classifier


def train_and_dump_model():
    here = os.path.dirname(os.path.abspath(__file__))
    path_model_dump = os.path.join(here, "model.pk")
    if os.path.exists(path_model_dump):
        return
    classifier = train_model()

    with open(path_model_dump, "wb") as f:
        pickle.dump(classifier, f)


if __name__ == "__main__":
    train_and_dump_model()
