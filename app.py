from flask import Flask, request, jsonify

app = Flask(__name__)

todos = [
    {'id': 1, 'task': 'Do laundry', 'complete': False},
    {'id': 2, 'task': 'Buy groceries', 'complete': True},
    # more todos...
]

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_todo():
    todo = request.get_json()
    todos.append(todo)
    return '', 200

@app.route('/todos/<int:index>', methods=['PUT'])
def update_todo(index):
    todo = request.get_json()
    todos[index] = todo
    return '', 204

@app.route('/todos/<int:index>', methods=['DELETE'])
def delete_todo(index):
    del todos[index]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)