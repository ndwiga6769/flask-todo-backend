from flask import Flask, request, jsonify

app = Flask(__name__)


tasks = []

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    task = {'id': len(tasks) + 1, 'text': data['text'], 'completed': False}
    tasks.append(task)
    return jsonify(task), 201

if __name__ == '__main__':
    app.run(debug=True)
