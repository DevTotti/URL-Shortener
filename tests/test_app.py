import json

def test_shorten_url(app, client):

    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }

    data = {
        "url":"https://dev.to/ndfishe/my-favorite-way-to-write-a-dockerfile-for-a-python-app-260i"
    }

    url = "/"

    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.content_type == mimetype
    assert response.json["encoded_url"] != ''


def test_short_url(app, client):

    response = client.get("/PvDpZx")
    assert response.status_code == 302