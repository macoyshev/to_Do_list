import pytest

from app.errors import IncorrectDescription, TaskNotFound
from app.services import TaskService


def test_redirect_from_main_page(client):
    response = client.get('/')

    assert response.status_code == 303


def test_get_tasks_code(client):
    response = client.get('/tasks')

    assert response.status_code == 200


def test_get_active_tasks_code(client):
    TaskService.create('test_1')

    response = client.get('/tasks?status=active')

    assert response.status_code == 200


def test_get_not_active_tasks_code(client):
    task = TaskService.create('test_1')
    task.is_active = False

    response = client.get('/tasks?status=not-active')

    assert response.status_code == 200


def test_post_task_code(client):
    response = client.post('/tasks', data={'description': 'test_description'})

    assert response.status_code == 303


@pytest.mark.parametrize(
    'description',
    ['test_description', 'test_description_1', 'test_description_2', 'something'],
)
def test_post_tasks(client, description):
    client.post('/tasks', data={'description': description})

    task = TaskService.get_by_id(0)

    assert task
    assert task.description == description


def test_patch_code(client):
    TaskService.create('test')
    response = client.patch('/tasks/0', data={'is_active': False})

    assert response.status_code == 303


def test_patch_tasks(client):
    TaskService.create('description_1')
    TaskService.create('description_2')

    client.patch('/tasks/0', data={'is_active': False})
    client.patch('/tasks/1', data={'is_active': False})

    task1 = TaskService.get_by_id(0)
    task2 = TaskService.get_by_id(1)

    assert task1
    assert task2
    assert not task1.is_active
    assert not task2.is_active


def test_patch_not_existing_tasks(client):
    with pytest.raises(TaskNotFound):
        client.patch('/tasks/0', data={'is_active': False})


def test_post_wrong_form(client):
    with pytest.raises(IncorrectDescription):
        client.post('/tasks', data={'wrong_field': 12312312})


def test_get_form_code(client):
    response = client.get('/new_task')

    assert response.status_code == 200
