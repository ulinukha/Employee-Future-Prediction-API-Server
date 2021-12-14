#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

loaded_model = pickle.load(open('finalized_model.sav', 'rb'))

@app.route('/', methods=['POST'])
def get_prediction():
    req_json = json.loads(request.data) #read request


    x = [req_json['data']]

    
    result = loaded_model.predict(x)
    result_float = [float(i) for i in result]
    return jsonify({'output': result_float}) # return model output
    
app.run(debug=True)