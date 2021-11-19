# -*- coding: utf-8 -*-

import os
import pickle

here = os.path.dirname(os.path.abspath(__file__))
path_model_dump = os.path.join(here, "model.pk")

with open(path_model_dump, "rb") as f:
    classifier = pickle.load(f)

X = [
    [6., 3.4],
    [6.7, 3.1],
    [6.3, 2.3],
]

pred = classifier.predict(X)
print(pred)
