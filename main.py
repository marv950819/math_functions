from flask import Flask
import numpy as np
import pandas as pd
from scipy import signal
import json


app = Flask(__name__)


def hello_world():
  return 'POR FIN MIERDA!'

@app.route('/hello_world')
def get_planner(coornenadas):
    df = coornenadas.convert_objects(convert_numeric=True)
    xs = df.y 
    data = np.sin(xs)
    peakind = signal.find_peaks_cwt(data, np.arange(0.1,1,0.1))
    xs[peakind]
    print(df.x[peakind])

data = json.load(open('datos.json'))
df = pd.DataFrame.from_dict(data, orient='index')
coordenadas_x_y = pd.DataFrame({'x':df.x[0],'y':df.y[0]})
coordenadas_x_y['xy'] = coordenadas_x_y.apply(lambda row: str(row.x)+str(row.y), axis=1)
get_planner(coordenadas_x_y)


if __name__ == '__main__':
  app.run()


