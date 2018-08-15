import json

from flask import render_template, session, redirect, url_for, request, jsonify, Response
from . import main
from app import db, csrf
from app.models import User, Project

import string
import random


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


@main.route('/', methods=['GET', 'POST'])
def home():
    print(request.method)
    params = ['project_title', 'year_1', 'year_2', 'year_3', 'year_4', 'year_5', 'justification', 'comments']
    fields = params[:]
    fields.insert(0, 'id')
    if request.method == 'POST':  # this block is only entered when the form is submitted
        project_id = request.args.get('project_id', int, None)
        project_create_update(params, project_id)
        return render_template('main/index.html', headers=fields)
    else:
        return render_template('main/index.html', headers=fields)


def project_create_update(params, project_id):
    if isinstance(project_id, int):
        project = Project.query.get(project_id)
    else:
        project = Project()
    print('project_id', project_id)
    print('POST: ')
    # project = Project()
    fields = []
    for param in params:
        field = request.form.get(param, None)
        if not field:
            field = None
        fields.append(field)
    if all(f is None for f in fields):
        pass
    else:
        project.project_title = fields[0]
        project.year_1 = fields[1]
        project.year_2 = fields[2]
        project.year_3 = fields[3]
        project.year_4 = fields[4]
        project.year_5 = fields[5]
        project.justification = fields[6]
        project.comments = fields[7]
        if isinstance(project_id, int):
            db.session.commit()
        else:
            db.session.add(project)
            db.session.commit()


@main.route('/get_data')
def get_data():
    def row2dict(row):
        """Given a row, it returns a dict."""
        d = {}
        for column in row.__table__.columns:
            d[column.name] = getattr(row, column.name)
        return d

    items = [list(row2dict(result).values()) for result in db.session.query(Project).all()]
    return jsonify(items=items)


# @csrf.exempt
@main.route('/delete_data/<int:param>', methods=['DELETE'])
def delete_data(param):
    print('param: ', param)
    # project = Project()
    project = Project.query.filter_by(id=param).first()
    db.session.delete(project)
    db.session.commit()
    return jsonify(status=True)


@main.route('login')
def add_user():
    user = User(email=id_generator(), username=id_generator())
    db.session.add(user)
    db.session.commit()
    return render_template('main/index.html')


def randString():
    return ''.join(random.choice())
