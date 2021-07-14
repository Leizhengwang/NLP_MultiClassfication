#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#import Flask
from flask import Flask, render_template, request
import joblib as joblib                    ##
#create an instance of Flask
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict/', methods=['GET','POST'])

def predict():
    if request.method == "POST":
        # get form data
        Job_description = request.form.get('Job_description')
        # call preprocessDataAndPredict and pass inputs
        try:
            prediction = preprocessDataAndPredict(Job_description)
            # pass prediction to template
            return render_template('predict.html', prediction=prediction)
        except ValueError:
            return "Please Enter valid values"
        pass
    pass


def preprocessDataAndPredict(Job_description):
    test_data = [Job_description]
    print(test_data)
    #open file
    file = open("lgclassifier.pkl","rb")
    #load trained model
    trained_model = joblib.load(file)
    #predict
    Id_to_Indus = {1: 'IT Consutlant software service',
                   2: 'Retial manuacturing',
                   3: 'Financial, insurance',
                   4: 'Federal, department and law',
                   5: 'Healthcare pharmaceutical',
                   6: 'High Tech'}
    prediction = Id_to_Indus[trained_model.predict(test_data)]

    return prediction
    pass
if __name__ == '__main__':
    app.run(debug=True)

