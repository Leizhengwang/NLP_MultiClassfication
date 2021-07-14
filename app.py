#!/usr/bin/env python
# coding: utf-8

# In[ ]:


//file: main.py
from flask import Flask, render_template, request

@app.route('/predict/', methods=['GET','POST'])
def predict():
    if request.method == "POST":
        #get form data
        Job_description = request.form.get('Job_description')
        return render_template('predict.html')
    pass