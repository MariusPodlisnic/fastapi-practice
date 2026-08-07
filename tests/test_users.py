import pytest
from fastapi import status
from app import schemas
from .database import client,session

@pytest.fixture
def test_user(client):
    user_data = {'email':"heyholetsgo@gmail.com",'password':"1234asf"}
    res = client.post("/users/",json=user_data)
    assert res.status_code == 201
    new_user = res.json()
    new_user['password'] = user_data['password']
    return new_user
def test_create_user(client):
    res = client.post("/users/",json = {"email":"heyholetsgo@gmail.com","password":"1234asf"})
    print(res.json())
    new_user = schemas.UserResponse(**res.json())
    assert res.status_code == 201

def test_login_user(client,test_user):
    res = client.post("/login", data={"username": test_user['email'], "password": test_user['password']})
