"""Basic testing all endpoints"""

import os
import requests

import db.utils as dbutils

BASE_URL = os.getenv("KANBAN_BOARD_URL", "http://localhost:5000")


def setup_module():
    dbutils.wipe_tasks()


def test_new():
    response = requests.post(f"{BASE_URL}/new", json={"name": "test1"})
    assert response.status_code == 201


def test_start():
    response = requests.post(f"{BASE_URL}/start", json={"name": "test1"})
    assert response.status_code == 200


def test_get_elapsed_time():
    response = requests.post(f"{BASE_URL}/get_elapsed_time",
                             json={"name": "test1"})
    assert response.status_code == 200


def test_resolve():
    response = requests.post(f"{BASE_URL}/resolve_task", json={"name": "test1"})
    assert response.status_code == 200


def test_get_cost():
    response = requests.post(f"{BASE_URL}/get_cost", json={"name": "test1"})
    assert response.status_code == 200


def test_get_tasks():
    response = requests.post(f"{BASE_URL}/get_tasks", json={"name": "test1"})
    assert response.status_code == 200