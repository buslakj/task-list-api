from .task import Task
from .goal import Goal
from flask import abort, make_response

def validate_id(task_id):
    try:
        task_id = int(task_id)
    except:
        return abort(make_response({"message": f"Task {task_id} is not valid"}, 400))
    task = Task.query.get(task_id)
    if not task:
        return abort(make_response({"message": f"Task {task_id} does not exist"}, 404))

    return task


def validate_goal_id(goal_id):
    try:
        goal_id = int(goal_id)
    except:
        return abort(make_response({"message": f"Goal {goal_id} is not valid"}, 400))
    goal = Goal.query.get(goal_id)
    if not goal:
        return abort(make_response({"message": f"Goal {goal_id} does not exist"}, 404))

    return goal

def validate_data(request_body):
    # return abort(make_response(f"Invalid data"),400)
    if 'title' not in request_body:
        return abort(make_response({"details":f"Invalid data"},400))
    elif 'description' not in request_body:
        return abort(make_response({"details":f"Invalid data"},400))
    return request_body

def validate_goal(request_body):
    if 'title' not in request_body:
        return abort(make_response({"details":f"Invalid data"},400))
    return request_body