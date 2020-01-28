from flask import Flask
from flask import request, jsonify, redirect, url_for
from werkzeug.utils import secure_filename
from keras.models import load_model
import pickle
from flask import render_template
import librosa
import librosa.display



app = Flask(__name__)
# Post Request
# process audiofile
# return 1 for unhealthy and Return 
#model = load_model('model.h5')
#filename = "heartbeat_disease_model_pkl.sav"
#loaded_model = pickle.load(open(filename, 'rb'))

#def pAudio():
    

@app.route('/server', methods = ['POST'])
def hello_world_sever():
    if request.method == 'POST':
        if 'file' not in request.files:
            #flash('No file part')

        #f = request.files['file']
         return 'You have a healthy Heart'

@app.route('/')
def hello_world():
    return render_template("kobe.html")

if __name__ == '__main__':
    app.run(debug=True)
