from flask import Flask, request, jsonify
import pickle
# instantiate Flask object
app = Flask(__name__)

# load previously saved logistic regression
with open('iris_logistic_regression.pkl','rb') as f:
    model = pickle.load(f)


# convert numerical predictions to Iris types
iris_types = ['setosa', 'versicolor', 'virginica']

# listen to POST commands on /api:
@app.route('/api',methods = ['POST'])
def predict():
    # params -- JSON object containing request parameters
    params = request.get_json(force = True)
    
    # transform parameters to a 2D input vector (list of lists)
    input_data = [[params['sepal_length'],params['sepal_width'],params['petal_length'],params['petal_width']]]
    
    # run prediction, convert to Iris type and return
    prediction = model.predict(input_data)[0]
    response = {"prediction":iris_types[prediction]}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

