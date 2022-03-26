from http import HTTPStatus

from flask import Blueprint, redirect, render_template, request
from werkzeug import Response

from app.services import TaskService

app = Blueprint('api', __name__, template_folder='templates')


@app.get('/')
def get_main_page() -> Response:
    return redirect('/tasks?status=active', code=HTTPStatus.SEE_OTHER)


@app.get('/tasks')
def get_tasks_board() -> str:
    status = request.args.get('status', default='all')
    tasks = TaskService.get_by_status(status=status)

    return render_template('index.html', tasks=tasks, status=status)


@app.get('/new_task')
def get_form() -> str:
    return render_template('new_task.html')


@app.post('/tasks')
def create_task() -> Response:
    description = request.form.get('description')

    TaskService.create(description)

    return redirect('/tasks?status=active', code=HTTPStatus.SEE_OTHER)


@app.patch('/tasks/<int:task_id>')
def update(task_id: int) -> Response:
    task = TaskService.get_by_id(task_id)

    task.is_active = False
    TaskService.update(task_entity=task)

    return redirect('/tasks?status=active', code=HTTPStatus.SEE_OTHER)
