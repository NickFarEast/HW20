from unittest.mock import MagicMock

from dao.director import DirectorDAO
from service.director import DirectorService

import pytest


@pytest.fixture
def director_dao():
    dao = DirectorDAO(None)
    dao.get_one = MagicMock()
    dao.get_all = MagicMock()

    return dao


@pytest.fixture
def director_service(director_dao):
    return DirectorService(dao=director_dao)


@pytest.mark.parametrize(
    'data', (

            {
                'id': 1,
                'name': 'test',
            },
            {
                'id': 2,
                'name': 'second name',
            }
    )
)
def test_get_one(director_service, data):
    director_service.dao.get_one.return_value = data

    assert director_service.get_one(1) == data


@pytest.mark.parametrize(
    'length, data',
    (
            (
                    2,
                    [
                        {
                            'id': 1,
                            'name': 'test',
                        },
                        {
                            'id': 2,
                            'name': 'test name',
                        },
                    ],

            ),
    ),
)
def test_get_all(director_service, length, data):
    director_service.dao.get_all.return_value = data
    test_result = director_service.get_all()
    assert isinstance(test_result, list)
    assert len(test_result) == length
    assert test_result == data
