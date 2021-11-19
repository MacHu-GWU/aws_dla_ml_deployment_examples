# -*- coding: utf-8 -*-

import os
import json
import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    """
    Hello world endpoint for connectivity test.
    """
    return "<p>Hello, World!</p>"


@app.route("/predict", methods=["POST", ])
def predict():
    """
    Take http post request, do prediction, return predicted labels.
    """
    data = json.loads(request.form["data"])
    here = os.path.dirname(os.path.abspath(__file__))
    path_model_dump = os.path.join(here, "model.pk")
    with open(path_model_dump, "rb") as f:
        classifier = pickle.load(f)
    pred = classifier.predict(data)
    response = {"pred": pred.tolist()}
    return json.dumps(response)
