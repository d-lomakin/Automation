import pytest
import requests

BASE_URL = "https://api.yougile.com/api-v2/projects"
API_KEY = "" # Вставить API ключ
USER_ID = "" # Вставить userId


def get_headers():
    return {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

@pytest.fixture
def create_project():
    url = BASE_URL
    data = {
        "title": "Проверочный проект",
        "users": {
            USER_ID: "admin"
        }
    }
    response = requests.post(url, json=data, headers=get_headers())
    assert response.status_code == 201
    project_id = response.json()["id"]
    return project_id

# Позитивные тесты

def test_create_project():
    url = BASE_URL
    data = {
        "title": "Новый проект",
        "users": {
            USER_ID: "admin"
        }
    }
    response = requests.post(url, json=data, headers=get_headers())
    assert response.status_code == 201
    response_data = response.json()
    assert "id" in response_data

def test_get_projects():
    url = BASE_URL
    response = requests.get(url, headers=get_headers())
    assert response.status_code == 200
    response_data = response.json()
    assert 'content' in response_data
    assert isinstance(response_data['content'], list)

def test_get_project_by_id(create_project):
    project_id = create_project
    url = f"{BASE_URL}/{project_id}"
    response = requests.get(url, headers=get_headers())
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["id"] == project_id

def test_update_project(create_project):
    project_id = create_project
    url = f"{BASE_URL}/{project_id}"
    data = {
        "title": "Измененный проект",
        "users": {
            USER_ID: "admin"
        }
    }
    response = requests.put(url, json=data, headers=get_headers())
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["id"] == project_id

# Негативные тесты

def test_create_project_without_title():
    url = BASE_URL
    data = {
        "users": {
            USER_ID: "admin"
        }
    }
    response = requests.post(url, json=data, headers=get_headers())
    assert response.status_code == 400

def test_update_project_without_id():
    url = f"{BASE_URL}/"
    data = {
        "title": "Проект без ID",
        "users": {
            USER_ID: "admin"
        }
    }
    response = requests.put(url, json=data, headers=get_headers())
    assert response.status_code == 404
