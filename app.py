from flask import Flask, jsonify
from flask import request
from util import DateConverter
from util import ListStringConverter
from util import ListIntConverter
from util import ListofRoutesConverter
from travel_planner_refactoring import finalResult
import datetime
app = Flask(__name__)





@app.route('/star')
def getStart():
	return "main"




if __name__ == '__main__':
    app.run(debug=True)

