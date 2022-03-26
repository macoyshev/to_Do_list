class TaskEntity:
    """
    Class represent task with the following fields:

    id: int

    description: str - description of a task

    is_active: str - completeness of a task
    """

    __id_counter = 0

    def __init__(self, description: str):
        """
        Returns new task with specified description.
        By default, 'is_active' field has false bool value.
        Id counted automatically, if you need reset id counter, call reset_id
        :param description: string description of tasks
        """
        self.id = TaskEntity.__id_counter
        self.description = description
        self.is_active = True

        TaskEntity.__id_counter += 1

    def __repr__(self) -> str:
        return f'id: {self.id}, task: {self.description}, active: {str(self.is_active).lower()}'

    @staticmethod
    def reset_id() -> None:
        """
        Function reset id counter,
        use the function if it is needed
        to clear lists, to count id again from 0
        """
        TaskEntity.__id_counter = 0
