from unittest.mock import MagicMock
from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.movie import MovieDAO
from service.director import DirectorService

import pytest

from service.genre import GenreService
from service.movie import MovieService


@pytest.fixture(autouse=True)
def director_dao():
    dao = DirectorDAO(None)
    dao.get_one = MagicMock()
    dao.get_all = MagicMock()
    dao.create = MagicMock()
    dao.update = MagicMock()
    dao.delete = MagicMock()
    return dao


@pytest.fixture(autouse=True)
def director_service(director_dao):
    return DirectorService(dao=director_dao)





@pytest.fixture(autouse=True)
def genre_dao():
    dao = GenreDAO(None)
    dao.get_one = MagicMock()
    dao.get_all = MagicMock()
    dao.create = MagicMock()
    dao.update = MagicMock()
    dao.delete = MagicMock()
    return dao


@pytest.fixture(autouse=True)
def genre_service(genre_dao):
    return GenreService(dao=genre_dao)


@pytest.fixture(autouse=True)
def movie_dao():
    dao = MovieDAO(None)
    dao.get_one = MagicMock()
    dao.get_all = MagicMock()
    dao.create = MagicMock()
    dao.update = MagicMock()
    dao.delete = MagicMock()
    return dao


@pytest.fixture(autouse=True)
def movie_service(movie_dao):
    return MovieService(dao=movie_dao)