# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pickle
from flask import Flask, jsonify, request,render_template,Response
import flask

data = pickle.load(open("test_data_2.pkl",'rb'))
lr   = pickle.load(open('lgbm_0.38596private.sav','rb'))
product_name_dict = pickle.load(open('producIdName.pkl','rb'))
    
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    to_predict_list = [int(x) for x in request.form.values()]
    order_number = to_predict_list[0]
    data1 = data[data.order_id==order_number]
    prediction = lr.predict(data1.drop(['order_id','user_id','product_id'],axis=1))
    data1['prediction'] = prediction
    data1 = data1[data1.prediction==1]
    output = []
    for i in data1.product_id:
        if i=='None':
            output.append('Nothing')
        else:
            output.append(product_name_dict[i])
    if len(output)==0:
        return Response(render_template('output.html',data=['Nothing']))
    else:
        return Response(render_template('output.html',data=output))
   

#return jsonify({'prediction': list(output)})


if __name__ == '__main__':
    app.run(debug=True)
    
