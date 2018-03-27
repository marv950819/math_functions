from flask import Flask, abort, request 
import numpy as np
import pandas as pd
from scipy import signal
import json


app = Flask(__name__)


# def getplanner(coornenadas):
# 	df = coornenadas.convert_objects(convert_numeric=True)
# 	xs = df.y 
# 	data = np.sin(xs)
# 	peakind = signal.find_peaks_cwt(data, np.arange(0.1,1,0.1))
# 	xs[peakind]
# 	print(df.x[peakind])


@app.route('/hello_world',methods=['POST'])
def hello_world():
	data = request.json
	coordenadas_x_y = pd.DataFrame.from_dict(data)
	coordenadas_x_y['xy'] = coordenadas_x_y.apply(lambda row: str(row.x)+str(row.y), axis=1)
	df = coordenadas_x_y.convert_objects(convert_numeric=True)
	xs = df.y 
	data = np.sin(xs)
	peakind = signal.find_peaks_cwt(data, np.arange(0.1,1,0.1))
	return df.x[peakind].to_json()	
	# if request.headers['Content-Type'] == 'text/plain':
	# 	return "Text Message: " + request.data
	# elif request.headers['Content-Type'] == 'application/json':
	# 	return "JSON Message: " + json.dumps(request.json)
	# else:
	# 	return "415 Unsupported Media Type ;)"


if __name__ == '__main__':
  	app.run()


