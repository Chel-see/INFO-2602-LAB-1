from flask import Flask, request, jsonify
import json

app = Flask(__name__)

global data

# read data from file and store in global variable data
with open('data.json') as f:
    data = json.load(f)


@app.route('/')
def hello_world():
    return 'Hello, World!'  # return 'Hello World' in response
  
##@app.route('/students')
##def get_students():
  ##  return jsonify(data)# return student data in response

@app.route('/students/<id>')
def get_student(id):
  for student in data: 
    if student['id'] == id: # filter out the students without the specified id
      return jsonify(student)
        
@app.route('/students')
def get_students():
  result = []
  pref = request.args.get('pref') # get the parameter from url
  if pref:
    for student in data: # iterate dataset
      if student['pref'] == pref: # select only the students with a given meal preference
        result.append(student) # add match student to the result
    return jsonify(result) # return filtered set if parameter is supplied
  return jsonify(data) # return entire dataset if no parameter supplied


  
@app.route('/stats')
def get_stats():
      stats = {  ##make dictionary for output and reference each loc, increase count 
        
          "Chicken": 0,
          "Fish": 0,
          "Vegetable": 0,
          "Computer Science (Major)": 0,
          "Computer Science (Special)": 0,
          "Information Technology (Major)": 0,
          "Information Technology (Special)": 0
      }

      for student in data:
          if student['pref'] == 'Chicken':
              stats["Chicken"] += 1
          elif student['pref'] == 'Fish':
              stats["Fish"] += 1
          elif student['pref'] == 'Vegetable':
              stats["Vegetable"] += 1

          if student['programme'] == 'Computer Science (Major)':
              stats["Computer Science (Major)"] += 1
          elif student['programme'] == 'Computer Science (Special)':
              stats["Computer Science (Special)"] += 1
          elif student['programme'] == 'Information Technology (Major)':
              stats["Information Technology (Major)"] += 1
          elif student['programme'] == 'Information Technology (Special)':
              stats["Information Technology (Special)"] += 1

      return jsonify(stats)


@app.route('/add/<int:a>/<int:b>')
def add(a, b):
      return jsonify({ "operation": "ADD", "a": a, "b": b, "result": a + b })

@app.route('/subtract/<int:a>/<int:b>')
def subtract(a, b):
      return jsonify({ "operation": "SUBTRACT", "a": a, "b": b, "result": a - b })

@app.route('/multiply/<int:a>/<int:b>')
def multiply(a, b):
      return jsonify({ "operation": "MULTIPLY", "a": a, "b": b, "result": a * b })

@app.route('/divide/<int:a>/<int:b>')
def divide(a, b):
      if b == 0:
          return jsonify({"error": "Division by zero is not allowed"})
      return jsonify({ "operation": "DIVIDE", "a": a, "b": b, "result": a / b })
      
      
  
    
app.run(host='0.0.0.0', port=8080, debug=True)
