from flask import Blueprint, jsonify, make_response, request
from requests import session
from app.models.task import Task
from app.models.helper import validate_id, validate_data
from app import db
from sqlalchemy import asc, desc

task_db = Blueprint("tasks",__name__, url_prefix = "/tasks")
# goal_db = Blueprint("goals", __name__, url_prefix = "/goals")

@task_db.route("", methods = ["GET"])
def get_all_tasks():
    task_response = []
    tasks = Task.query.all()
    for task in tasks:
        task_response.append(task.to_json())
    return jsonify(task_response), 200

@task_db.route("?sort=asc", methods = ["GET"])
def sort_all_tasks_asc():
    task_response = []
    ordered_tasks = Task.query.order_by(asc(Task.title)).all()
    for task in ordered_tasks:
        task_response.append(task.to_json())
    return jsonify(task_response), 200

@task_db.route("?sort=desc", methods = ["GET"])
def sort_all_tasks_desc():
    task_response = []
    ordered_tasks = Task.query.order_by(desc(Task.title))
    for task in ordered_tasks:
        task_response.append(task.to_json())
    print(ordered_tasks)
    return jsonify(task_response), 200


@task_db.route("/<task_id>", methods = ["GET"])
def get_one_task(task_id):
    task_response = []
    task = validate_id(task_id)
    return jsonify({"task": task.to_json()}), 200

@task_db.route("", methods = ["POST"])
def create_one_response():
    request_body = request.get_json()
    valid_data = validate_data(request_body)
    new_task = Task.create_task(request_body)
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"task":new_task.to_json()}), 201
    

@task_db.route("/<task_id>", methods = ["PUT"])
def update_task(task_id):
    task = validate_id(task_id)
    request_body = request.get_json()
    task.update_task(request_body)
    db.session.commit()
    return jsonify({"task":task.to_json()}), 200
    # make_response(f"Task {task_id} successfully updated"), 201

@task_db.route("/<task_id>", methods = ["DELETE"])
def delete_task(task_id):
    task = validate_id(task_id)
    task_title = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()
    return {
        "details": f'Task {task_id} \"{task_title.title}\" successfully deleted'}, 200 
    # make_response(f"Task {task_id} successfully deleted"), 201

@task_db.route("/<task_id>/mark_complete", methods = ["PATCH"])
def mark_task_complete(task_id, mark_complete):
    task = validate_id(task_id)
    if mark_complete == "mark_incomplete": 
        completed_at = False
    elif mark_complete == "mark_complete":
        completed_at == False
    request_body = request.get_json()
    task.update_task(request_body)
    db.session.commit()
    return jsonify({"task":task.to_json()}), 200