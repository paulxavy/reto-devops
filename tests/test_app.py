import pytest
from fastapi.testclient import TestClient
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.main import app
from app.config import API_KEY, JWT_SECRET, JWT_ALGORITHM
import jwt
import time
import uuid

client = TestClient(app)

def gen_jwt(exp=60):
    now = int(time.time())
    payload = {"jti": str(uuid.uuid4()), "iat": now, "nbf": now, "exp": now + exp}
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

def test_wrong_method_returns_error():
    res = client.get("/DevOps")
    assert res.status_code == 405
    assert res.text == "ERROR"

def test_missing_api_key():
    token = gen_jwt()
    res = client.post("/DevOps", headers={"X-JWT-KWY": token, "Content-Type":"application/json"},
                      json={"message":"x","to":"Juan","from":"Rita","timeToLifeSec":10})
    assert res.status_code == 401

def test_missing_jwt():
    res = client.post("/DevOps", headers={"X-Parse-REST-API-Key": API_KEY, "Content-Type":"application/json"},
                      json={"message":"x","to":"Juan","from":"Rita","timeToLifeSec":10})
    assert res.status_code == 401

def test_success():
    token = gen_jwt()
    payload = {"message":"This is a test","to":"Juan Perez","from":"Rita Asturia","timeToLifeSec":45}
    res = client.post("/DevOps", headers={"X-Parse-REST-API-Key": API_KEY, "X-JWT-KWY": token},
                      json=payload)
    assert res.status_code == 200
    assert res.json() == {"message":"Hello Juan Perez your message will be sent"}
