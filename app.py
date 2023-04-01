from flask import Flask,request,render_template,jsonify
from flask_restful import Resource,Api
from PIL import Image
import numpy as np 
import pickle

app = Flask(__name__)


diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

@app.route('/')
def method_name():
    return render_template('diabetic.html')

def ValuePredictor(to_predict_list):
	to_predict = np.array(to_predict_list).reshape(1, 8)
	result = diabetes_model.predict(to_predict)
	return result[0]

@app.route('/resultApi', methods=['POST'])
def Api():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        result = ValuePredictor(to_predict_list)
        	
        return jsonify({'prediction':prediction})
         
    	
			
				
		
    
    	
	       
 	
@app.route('/result', methods = ['POST'])
def results():
	if request.method == 'POST':
		to_predict_list = request.form.to_dict()
		to_predict_list = list(to_predict_list.values())
		to_predict_list = list(map(int, to_predict_list))
		result = ValuePredictor(to_predict_list)
  	
		if int(result)== 1:
			prediction ='The person is diabetic'
		else:
			prediction ='The person is NOT diabetic'		
		return render_template("diabetic.html",prediction = prediction)


 
if __name__ == '__main__':

	app.run()
