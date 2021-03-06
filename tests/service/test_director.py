
import pytest


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


@pytest.mark.parametrize(
    'original_data, modified_data',
    (

            (
                    {
                        'id': 1,
                        'name': 'test',
                    },
                    {
                        'id': 1,
                        'name': 'changed name',
                    }
            ),
    )
)
def test_partially_update(director_service, original_data, modified_data):
    director_service.dao.get_one.return_value = original_data
    director_service.partially_update(modified_data)

    director_service.dao.update.assert_called_once_with(modified_data)

@pytest.mark.parametrize(
    'data', (

            {
                'name': 'test',
            },
    )
)
def test_create(director_service, data):
    director_service.dao.create(data)
    director = director_service.create(data)
    assert director.id is not None

def test_delete(director_service):
    director_service.delete(1)
    director_service.dao.delete.assert_called_once_with(1)



def test_update(director_service):
    director_service.update({})
    director_service.dao.update.assert_called_once_with({})