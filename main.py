from flask import Flask
from flask import jsonify
from flask_restful import reqparse

#import runBatch

app = Flask(__name__)

@app.route('/')
def index():
  return "Hej"


@app.route('/analyze', methods=['POST'])
def analyze():
  parser = reqparse.RequestParser()
  parser.add_argument('path')
  args = parser.parse_args()
  print("Arguments: ", args['path']) 
  
  return jsonify({'message':'hej igen'})


if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)
  


  
  