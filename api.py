from flask import Flask, jsonify, request
import dbfunctions

app = Flask(__name__)
app.secret_key = "veryverysecret"


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/listtasks')
def ListTasks():
    tasks = dbfunctions.show_tasks()
    for task in tasks:
        print(task[0])
    # need to convert tasks into a dictionary to 'help' jsonify
    return jsonify(tasks)


@app.route('/listtasks/<new_task>')
def GetTask(new_task):
    task = [task for task in dbfunctions.show_tasks() if task[0] == new_task]
    if len(task) == 1:
        return jsonify(task[1])
    else:
        dbfunctions.add_new_task(new_task)
        response = jsonify({'message': 'new task added: ' + new_task})
        response.status_code = 404
        return response


@app.route('/listtasks', methods=['DELETE'])
def CreateTask():
    if request.headers['Content-Type'] == 'application/json':
        new_task = request.json
        dbfunctions.add_new_task(new_task)
        return jsonify(new_task)
    else:
        response = jsonify({'message': "Invalid Request"})
        response.status_code = 404
        return response


@app.route('/listtasks/<task>', methods=['PUT'])
def UpdateTask(new_task):
    dbfunctions.remove_task(new_task)
    if request.headers['Content-Type'] == 'application/json':
        new_task = request.json
        dbfunctions.add_new_task(new_task)
        return jsonify(new_task)
    else:
        response = jsonify({'message': "Invalid Request"})
        response.status_code = 404
        return response



if __name__ == '__main__':

    app.run()
