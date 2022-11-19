import numpy as np
import json
from flask import Flask, render_template, request

from tensorflow.python.keras.models import load_model

app = Flask(__name__)




import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "1gwmabI1uLfI58p348zk2GOm5l-4Gq-30YwWSKgGvsUY"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
# payload_scoring = {"input_data": [{"fields": [array_of_input_fields], "values": [array_of_values_to_be_scored, another_array_of_values_to_be_scored]}]}

# response_scoring = requests.post('https://eu-gb.ml.cloud.ibm.com/ml/v4/deployments/2006243c-d8cb-4ad4-9f79-69698be3f014/predictions?version=2022-11-18', json=payload_scoring,
#  headers={'Authorization': 'Bearer ' + mltoken})
# print("Scoring response")
# response_scoring.json()





# model = load_model('crude_oil_forecasting.h5')
ent = []

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=["GET", "POST"])
def home1():
    if request.method == "POST":
        data = request.form['data']
        # print(data)
        ent.append(data)
        
        inp = str(request.form['data'])
        inp = inp.split(',')
        for i in range(0, len(inp)):
            inp[i] = float(inp[i])
        inp = np.array(inp).reshape(1,-1)
        temp = list(inp)
        temp = temp[0].tolist()
        # print(temp)
        outpt = []
        n_steps = 10
        i=0
        while(i<1):
            if(len(temp) > 10):
                #some prblm
                inp = np.array(temp[1:])
                print("{} day input {}".format(i, inp))
                inp = inp.reshape(1,-1)
                inp = inp.reshape((1, n_steps, 1))

                payload_scoring = {"input_data": [{"fields": ["price"], "values": inp}]}
                response_scoring = requests.post('https://eu-gb.ml.cloud.ibm.com/ml/v4/deployments/2006243c-d8cb-4ad4-9f79-69698be3f014/predictions?version=2022-11-18', json=payload_scoring,
                headers={'Authorization': 'Bearer ' + mltoken})
                print("Scoring response")
                yhat = response_scoring.json()

                # yhat = model.predict(inp, verbose=0)
                temp.extend(yhat[0].tolist())
                temp = temp[1:]
                outpt.extend(yhat.tolist())
                i += 1
            else:
                inp = inp.reshape((1,len(temp),1)) #n_steps --> len(temp)
                # yhat = model.predict(inp, verbose=0)

                payload_scoring = {"input_data": [{"fields": ["price"], "values": inp}]}
                response_scoring = requests.post('https://eu-gb.ml.cloud.ibm.com/ml/v4/deployments/2006243c-d8cb-4ad4-9f79-69698be3f014/predictions?version=2022-11-18', json=payload_scoring,
                headers={'Authorization': 'Bearer ' + mltoken})
                print("Scoring response")
                yhat = response_scoring.json()
                outpt.extend(yhat.tolist())
                temp.extend(yhat[0].tolist())
                outpt.extend(yhat.tolist())
                i+=1
            

        return render_template("predict_opt.html", entries = outpt)
    else:
        return render_template("predict_opt.html")

@app.route('/market')
def home2():
    return render_template("market.html")


if __name__ == '__main__':
    app.run(debug=True)