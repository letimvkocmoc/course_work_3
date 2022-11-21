from _pytest.fixtures import fixture
from main import app


@fixture()
def client():

    return app.test_client()


@fixture()
def post_keys():

    return {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}