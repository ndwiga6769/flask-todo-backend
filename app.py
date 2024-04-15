from flask import Flask, request, jsonify, abort

app = Flask(__name__)

tasks = []

# Routes for CRUD operations
@app.route('/tasks', methods=['GET'])
def get_tasks():
    # Retrieve all tasks
    pass

@app.route('/tasks', methods=['POST'])
def add_task():
    # Add a new task
    pass

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    # Retrieve a specific task by ID
    pass

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    # Update a specific task by ID
    pass

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    # Delete a specific task by ID
    pass

if __name__ == '__main__':
    app.run(debug=True)
