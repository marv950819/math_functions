from flask import Flask
import numpy as np

app = Flask(__name__)

@app.route('/hello_world')
def hello_world():
  return 'POR FIN MIERDA!'

if __name__ == '__main__':
  app.run()