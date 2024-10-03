import requests

BASE_URL = "https://api.yougile.com/api-v2/projects"
API_KEY = ""  # Вставить API ключ 


def get_headers():
    return {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }


project_id = None

# Позитивные тесты


def test_create_project():
    global project_id
    url = BASE_URL
    data = {
        "title": "Проверочный проект",
        "users": {
            "": "admin"  # Вставить userId
        }
    }
    response = requests.post(url, json=data, headers=get_headers())

    assert response.status_code == 201
    assert "id" in response.json()
    project_id = response.json()["id"]


def test_get_projects():
    url = BASE_URL
    response = requests.get(url, headers=get_headers())

    assert response.status_code == 200
    response_data = response.json()

    assert 'content' in response_data
    assert isinstance(response_data['content'], list)


def test_get_project_by_id():
    global project_id
    url = f"{BASE_URL}/{project_id}"
    response = requests.get(url, headers=get_headers())

    assert response.status_code == 200
    response_data = response.json()
    assert response_data["id"] == project_id


def test_update_project():
    global project_id
    url = f"{BASE_URL}/{project_id}"
    data = {
        "title": "Измененный проект",
        "users": {
            "": "admin"  # Вставить userId
        }
    }
    response = requests.put(url, json=data, headers=get_headers())

    assert response.status_code == 200
    response_data = response.json()
    assert "id" in response_data
    assert response_data["id"] == project_id

# Негативные тесты


def test_create_project_without_title():
    url = BASE_URL
    data = {
        "users": {
            "": "admin"  # Вставить userId
        }
    }
    response = requests.post(url, json=data, headers=get_headers())

    assert response.status_code == 400


def test_update_project_without_id():
    url = f"{BASE_URL}/"
    data = {
        "title": "Измененный проект без ID",
        "users": {
            "": "admin"  # Вставить userId
        }
    }
    response = requests.put(url, json=data, headers=get_headers())

    assert response.status_code == 404
