from flask import Flask, render_template, request, json
import os
import sys
import tensorflow as tf

from settings import PROJECT_ROOT
from botpredictor import BotPredictor

app = Flask(__name__)

@app.route("/")
def main():

    return render_template('index.html')

@app.route("/chat", methods=['POST'])
def chat():
    corp_dir = os.path.join(PROJECT_ROOT, 'Data', 'Corpus')
    knbs_dir = os.path.join(PROJECT_ROOT, 'Data', 'KnowledgeBase')
    res_dir = os.path.join(PROJECT_ROOT, 'Data', 'Result')

    with tf.Session() as sess:
        predictor = BotPredictor(sess, corpus_dir=corp_dir, knbase_dir=knbs_dir,
                                 result_dir=res_dir, result_file='basic')

        question = request.json['message']
        session_id = predictor.session_data.add_session()
        answer = predictor.predict(session_id, question)

    return json.dumps({'response': answer})

if __name__ == "__main__":
    app.run()
