from flask import Flask, request, jsonify

app = Flask(__name__)

todos = {
    1: {'id': 1, 'task': 'Do laundry', 'complete': False},
    2: {'id': 2, 'task': 'Buy groceries', 'complete': True},
    # more todos...
}

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_todo():
    todo = request.get_json()
    todos[todo['id']] = todo
    return todo, 200

@app.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    todo = request.get_json()
    
    if id in todos:
        todos[id] = todo
        return '', 204
    else:
        return f"Todo with id {id} not found.", 404

@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    if id in todos:
        del todos[id]
        return '', 204
    else:
        return f"Todo with id {id} not found.", 404

if __name__ == '__main__':
    app.run(debug=True)