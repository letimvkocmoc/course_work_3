def test_posts(client):
    """
    Функция, с помощью которой происходит тестирование по запросу /api/posts.
    Получаем отклик от страницы, проверяем, что полученный результат в формате списка
    """

    response = client.get('/api/posts/')
    assert response.status_code == 200
    assert isinstance(response.json, list)


def test_post(client, post_keys):
    """
    Функция, с помощью которой происходит тестирование по запросу конкретного поста /api/posts/<postid>.
    Получаем отклик от страницы, проверяем, что полученный результат в формате словаря с нужными нам ключами.
    Ключи указаны в фикстуре post_keys
    """

    response = client.get('/api/posts/1')
    assert response.status_code == 200
    assert isinstance(response.json, dict)
    assert set(response.json.keys()) == post_keys

