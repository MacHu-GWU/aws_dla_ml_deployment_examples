# -*- coding: utf-8 -*-

import os
import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    return "<p>Hello, World!</p>"


@app.route("/predict", methods=["POST", ])
def predict():
    print(request.form)
    print(dict(request.form))
    return "good"
    # here = os.path.dirname(os.path.abspath(__file__))
    # path_model_dump = os.path.join(here, "model.pk")
    # with open(path_model_dump, "rb") as f:
    #     classifier = pickle.load(f)
