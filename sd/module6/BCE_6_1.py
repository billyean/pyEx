from flask import (Flask, request, abort, Response, json, jsonify)
app = Flask(__name__)


class Student:
    def __init__(self, student_id, name, email=None, tel=None):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.tel = tel

    def json(self):
        return json.dumps({
            'id': self.student_id,
            'name': self.name,
            'email': self.email,
            'tel': self.tel
        })


students = []


@app.route('/student', methods=['GET'])
def get_students():
    return Response(students, status=200, mimetype='application/json')


@app.route('/student/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    match_id = [x for x in students if x.student_id == student_id]
    if len(match_id) == 0:
        abort(404)
    else:
        return Response(match_id[0], status=200, mimetype='application/json')


@app.route('/student', methods=['POST'])
def create_student():
    try:
        data = json.loads(request.data)
        print(data)
        student_id = data['id']
        name = data['name']
        email = None
        if 'email' in data:
            email = data['email']
        tel = None
        if 'tel' in data:
            tel = data['tel']

        if len(students) > 0:
            match_id = [x for x in students if x.student_id == student_id]

            if len(match_id) > 0:
                abort(409)

        student = Student(student_id, name, email, tel)
        students.append(student)

        return Response(student.json(), status=201, mimetype='application/json')
    except Exception as e:
        print(e)
        return Response(e, status=500)


@app.route('/student/<int:student_id>', methods=['POST'])
def update_student(student_id):
    try:
        match_id = [x for x in students if x.student_id == student_id]
        if len(match_id) == 0:
            abort(404)

        data = json.loads(request.data)
        name = data['name']
        email = None
        if 'email' in data:
            email = data['email']
        tel = None
        if 'tel' in data:
            tel = data['tel']
        student = Student(student_id, name, email, tel)

        match_idx = [index for (index, x) in enumerate(students) if x.student_id == student_id]

        if len(match_idx) == 0:
            abort(404)

        for index in match_idx:
            students[index] = student

        return Response(student.json(), status=200, mimetype='application/json')
    except Exception as e:
        print(e)
        return Response(e, status=500)


@app.route('/student/<int:student_id>', methods=['GET'])
def get_student_by_id(student_id):
    match_id = [x for x in students if x.student_id == student_id]
    if len(match_id) == 0:
        abort(404)
    else:
        return Response(match_id[0].json(), status=200, mimetype='application/json')


@app.route('/student/<string:name>', methods=['GET'])
def get_student_by_name(name):
    print(name)
    match_id = [x for x in students if x.name == name]
    if len(match_id) == 0:
        abort(404)
    else:
        return Response(match_id[0].json(), status=200, mimetype='application/json')


if __name__ == "__main__":
    app.run()
