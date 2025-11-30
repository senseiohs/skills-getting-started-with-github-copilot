
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from app import app
import pytest
from fastapi.testclient import TestClient

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_signup_for_activity():
    activity = list(client.get("/activities").json().keys())[0]
    email = "testuser@mergington.edu"
    response = client.post(f"/activities/{activity}/signup?email={email}")
    assert response.status_code == 200 or response.status_code == 400
    response2 = client.post(f"/activities/{activity}/signup?email={email}")
    assert response2.status_code == 400

def test_unregister_for_activity():
    activity = list(client.get("/activities").json().keys())[0]
    email = "testuser@mergington.edu"
    response = client.post(f"/activities/{activity}/unregister?email={email}")
    assert response.status_code == 200 or response.status_code == 400
