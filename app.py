from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model_file = open('model.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
    return render_template('index.html', predict_covid='')

@app.route('/predict', methods=['POST'])
def predict():
    '''
    Predict the insurance cost based on user inputs
    and render the result to the html page
    '''
    age, intubed, pneumonia, diabetes, hypertension = [x for x in request.form.values()]

    data = []

    data.append(int(age))
    if intubed == 'Ya':
        data.extend([0, 1])
    else:
        data.extend([1, 0])

    if pneumonia == 'Ya':
        data.extend([0, 1])
    else:
        data.extend([1, 0])
        
    if diabetes == 'Ya':
        data.extend([0, 1])
    else:
        data.extend([1, 0])
        
    if hypertension == 'Ya':
        data.extend([0, 1])
    else:
        data.extend([1, 0])
    
    prediction = model.predict([data])
    output = round(prediction[0], 2)

    return render_template('index.html', predict_covid=output, intubed=intubed, pneumonia=pneumonia, diabetes=diabetes, hypertension=hypertension)


if __name__ == '__main__':
    app.run(debug=True)
