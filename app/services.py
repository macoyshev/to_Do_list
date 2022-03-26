import sys
from typing import Optional

from loguru import logger

from app.errors import IncorrectDescription, TaskNotFound
from app.models import TaskEntity

tasks: list[TaskEntity] = []  # temporary storage of tasks

logger.remove()
logger.add(
    sys.stdout,
    format='<blue>{time:hh:mm:ss.SS} | {level} | {name}:{function}:{line} | {message}</blue>',
    level='DEBUG',
)


class TaskService:
    """
    Class contains methods for operations under tasks
    """

    @staticmethod
    def get_by_id(task_id: int) -> TaskEntity:
        """
        :param task_id: id of a task
        :return: task with specified id
        """
        for task in tasks:
            if task.id == task_id:
                return task

        logger.error(f'there is no such task with id: {id}')

        raise TaskNotFound()

    @staticmethod
    def get_by_status(status: str = 'active') -> list[TaskEntity]:
        """
        :param status: one of the following stations: [active, not-active, all]
        :return: list of tasks filtered by status
        """
        res: list[TaskEntity] = []

        if status == 'active':
            res = list(filter(lambda t: t.is_active, tasks))

        if status == 'not-active':
            res = list(filter(lambda t: not t.is_active, tasks))

        if status == 'all':
            res = tasks

        return res

    @staticmethod
    def create(description: Optional[str]) -> TaskEntity:
        """
        Creates new task and adds this in list of tasks
        :param description: string description of a task
        :return: new task
        """
        if not description:
            logger.error('description is not provided')

            raise IncorrectDescription()

        new_task = TaskEntity(description)
        tasks.append(new_task)

        logger.info(f'task was added: {new_task}')

        return new_task

    @staticmethod
    def update(task_entity: Optional[TaskEntity]) -> None:
        """
        Updates task with task_entity in list of tasks
        :param task_entity: object of list of tasks with another state
        """
        for index, task in enumerate(tasks):
            if task == task_entity:
                tasks[index] = task_entity

        logger.info(f'task was updated: {task_entity}')
