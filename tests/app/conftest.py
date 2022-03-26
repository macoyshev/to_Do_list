import pytest

from app import create_app
from app.models import TaskEntity
from app.services import tasks


@pytest.fixture()
def client():
    app = create_app()
    app.config.update(
        {
            'TESTING': True,
        }
    )

    yield app.test_client()

    tasks.clear()
    TaskEntity.reset_id()
