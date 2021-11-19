# -*- coding: utf-8 -*-

import json
import requests

# test connectivity using hello world endpoint
res = requests.get("http://127.0.0.1:5000")
print(res.text)

# test ML prediction, send a test data, returns label
# test data format: 2d-array
data = [
    [6., 3.4],
    [6.7, 3.1],
    [6.3, 2.3],
]
res = requests.post("http://127.0.0.1:5000/predict", data={"data": json.dumps(data)})
print(res.text)
