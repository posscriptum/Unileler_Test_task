#from flask import Flask

#app = Flask(__name__)


#@app.route('/', methods = ['GET'])
#def hello_world():
 #   return 'Hello World!'


#if __name__ == '__main__':
from app import app
app.run()
