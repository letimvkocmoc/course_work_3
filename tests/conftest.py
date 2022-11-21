from _pytest.fixtures import fixture
from main import app


@fixture()
def client():
    """Фикстура для тестирования отклика по запросу"""

    return app.test_client()


@fixture()
def post_keys():
    """Фикстура для сверки наличия нужных ключей по запросу"""

    return {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}