def test_posts(client):

    response = client.get('/api/posts/')
    assert response.status_code == 200
    assert isinstance(response.json, list)


def test_post(client, post_keys):

    response = client.get('/api/posts/1')
    assert response.status_code == 200
    assert isinstance(response.json, dict)
    assert set(response.json.keys()) == post_keys

