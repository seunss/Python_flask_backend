from flask import Flask
from flask import request, jsonify, redirect, url_for
from werkzeug.utils import secure_filename
from flask_restplus import Api, Resource, fields
#from keras.models import load_model
import pickle
from flask import render_template
#import librosa
#import librosa.display
#import tflite_runtime.interpreter as tflite





flask_app = Flask(__name__)
app = Api(app = flask_app, version ="1.1", title = 'Heart Beat API', description ="Classify Heart beat sounds using MFCC coeffients" )
name_space = app.namespace('Heart',description = "Heart Beat API")


model = app.model('Heart Model',
					{'name': fields.String(required = True,
											description = "Name of the person",
											help = "Name cannot be blank"),
					 'mfcc': fields.List(fields.Integer(required = True, 
				  							description="List of MFCC coeffients", 
    					  				 	help="Select 2 cannot be blank"))})

# Post Request,
# process audiofile
# return 1 for unhealthy and Return 
#model = load_model('model.h5')
#filename = "heartbeat_disease_model_pkl.sav"
#loaded_model = pickle.load(open(filename, 'rb'))

def classify(audio):
    #y, sr = librosa.load(audio, duration=4)
    #mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
    return 1

#def pAudio():
    

@app.route('/server', methods = ['POST'])
class MainClass(Resource):
	def get(self):
		return {
			"status": "Got new data"
		}
	
	@app.expect(model)
	def post(self):
		try:
			mfccc = request.json['mfcc']
			status = classify(mfccc)
			return {
			"status": "Posted new data" + status
			}
		except KeyError as e:
			name_space.abort(500, e.__doc__, status = "Could not save information", statusCode = "500")

