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
def test_get_one(movie_service, data):
    movie_service.dao.get_one.return_value = data

    assert movie_service.get_one(1) == data


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
def test_get_all(movie_service, length, data):
    movie_service.dao.get_all.return_value = data
    test_result = movie_service.get_all()
    assert isinstance(test_result, list)
    assert len(test_result) == length
    assert test_result == data


@pytest.mark.parametrize(
    'original_data, modified_data',
    (

            (
                    {
                        'id': 1,
                        'title': 'test',
                        'description' : 'test',
                        'trailer' :'test',
                        'year' : 2000,
                        'rating' : 'test',
                    },
                    {
                        'id': 1,
                        'title': 'test 2',
                        'description' : 'test2',
                        'trailer' :'test2',
                        'year' : 2000,
                        'rating' : 'test2',
                    }
            ),
    )
)
def test_partially_update(movie_service, original_data, modified_data):
    movie_service.dao.get_one.return_value = original_data
    movie_service.partially_update(modified_data)

    movie_service.dao.update.assert_called_once_with(modified_data)


@pytest.mark.parametrize(
    'data', (

            {
                'name': 'test',
            },
    )
)
def test_create(movie_service, data):
    movie_service.dao.create(data)
    movie = movie_service.create(data)
    assert movie.id is not None


def test_delete(movie_service):
    movie_service.delete(1)
    movie_service.dao.delete.assert_called_once_with(1)


def test_update(movie_service):
    movie_service.update({})
    movie_service.dao.update.assert_called_once_with({})
