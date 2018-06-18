# seq2seq-chatbot
A sequence to sequence chatbot built using tensorflow. This is a college project built by using various sources and 
tutorials. This repository contains a much better explanation of this implementation and is the inspiration for this project 
https://github.com/bshao001/ChatLearner .

## Dependencies
The model has been tested with
1. Tensorflow = 1.4
2. Python = 3.5
3. Numpy
4. Recommended to use a virtual python environment such as Anaconda or virtual env
5. pip freeze > requirements.txt and installing using pip install -r requirements.txt is a quick way install all dependencies

## Trained model
Link for the trained model will be provided soon

## Training you own model
run - python bottrainer.py 
To train the model. A folder named Result must be created inside the Data folder before training inside which the trained 
models will be trained.

## Testing the model
run - python botui.py
To test the model on a console. The > prompt is the input indicator and your input will be read by the console after the enter
key. The generated response will be displayed below each input.

## Testing using the Flask web ui
### Dependencies for Flask app
1. Flask - 1.0.2 - pip install flask

run - python app.py to start a local flask server on http://127.0.0.1:5000.
A simple ui is used with bootstrap.

## To do
1. Expand the scope of the conversational model and the rules
2. Make the model compatible for Tensorflow mobile
3. Built a better web ui
4. Add model to a Facebook messenger bot

## Credits and References
1. Chatleaner by bshao001 https://github.com/bshao001/ChatLearner
