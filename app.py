from flask import Flask
from flask import request, jsonify, redirect, url_for
from werkzeug.utils import secure_filename
#from keras.models import load_model
from sklearn.neighbors import KNeighborsClassifier
import pickle
import numpy as np
from flask import render_template
import librosa
from sklearn.externals import joblib
#import librosa.display
#import tflite_runtime.interpreter as tflite





app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024 #Prevent audio bigger than 10MB
# Post Request
# process audiofile
# return 1 for unhealthy and Return 
#model = load_model('model.h5')
filename = "joblibheartbeat_diseaseKNN.sav"
#loaded_model = pickle.load(open(filename, 'rb'))
loaded_model = joblib.load(filename)
predictorWorking = True
def predictor(mfccs):
     x1 = []
     x1.append(mfccs)
     x1 = np.asarray(x1)
     print("X train:", x1.shape)
     x1Size = len(x1)
     x1 = x1.reshape(x1Size,-1)
     print("X train:", x1.shape)
     try:
        y = loaded_model.predict(x1)
        print(y)
        if y[0] == 0:
            return False
        

        
     except:
         print('Something went wrong')
         predictorWorking = False
         return True

     return True



def features_file(audio):
    y, sr = librosa.load(audio, duration=4)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
    predict = predictor(mfccs)
    return predict

#def pAudio():
@app.route('/coleworld', methods = ['POST','GET'])
def moblie():
    if request.method == 'POST' or request.method == 'GET':
        predictorWorking = True
        if 'm' not in request.files:
            print(request.files)
            print(request)
            return 'no file found'

        f = request.files['m']
        x = features_file(f)
        if predictorWorking:
            if x:
                return jsonify("Healthy Heart")
            else:
                return jsonify("Murmur Detected")
        else:
            return jsonify("Server Not working")
        return jsonify('You have a healthy Heart')



@app.route('/server', methods = ['POST'])
def hello_world_sever():
    if request.method == 'POST':
        predictorWorking = True
        if 'm' not in request.files:
            print(request.files)
            print(request)
            return 'no file found'

        f = request.files['m']
        x = features_file(f)
        if predictorWorking:
            if x:
                return "Healthy Heart"
            else:
                return "Murmur Detected"
        else:
            return "Server Not working"
        return 'You have a healthy Heart'

@app.route('/')
def hello_world():
    return render_template("kobe.html")

if __name__ == '__main__':
    app.run(threaded=True, port=5000)
