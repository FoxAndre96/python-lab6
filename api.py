from flask import Flask, jsonify, request
import dbfunctions

app = Flask(__name__)
app.secret_key = "veryverysecret"


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/listtasks')
def ListTasks():
    # get list of object into a python variable (here already created)
    tasks = dbfunctions.show_tasks()
    return jsonify(tasks)


@app.route('/listtasks/<new_task>')
def GetTask(new_task):
    task = [task for task in dbfunctions.show_tasks() if task[1] == new_task]
    if len(task) == 1:
        return jsonify(task[1])
    else:
        response = jsonify({'message': 'user not found: ' + name})
        response.status_code = 404
        return response


@app.route('/listtasks', methods=['POST'])
def CreateTask():
    if request.headers['Content-Type'] == 'application/json':
        new_task = request.json
        dbfunctions.add_new_task(new_task)
        return jsonify(new_task)
    else:
        response = jsonify({'message': "Invalid Request"})
        response.status_code = 404
        return response


if __name__ == '__main__':

    app.run(port=5004)
