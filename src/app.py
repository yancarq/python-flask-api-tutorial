from flask import Flask,jsonify,request,json

app = Flask(__name__)

todos = [{"label": "My first task", "done": False },
         { "label": "My second task", "done": False }]

@app.route('/todos', methods=['GET'])
def hello_world():
    # supongamos que tienes cierta información (some_data) en una variable json

    # puedes convertir esa variable en un string json así
    json_text = jsonify(todos)

    # y luego puedes retorarla (return) en el response body así:
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    decoded_object = json.loads(request_body)
    
    print("Incoming request with the following body", request_body)
    todos.append(decoded_object)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    todos.pop(position)
    return jsonify(todos)

# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)