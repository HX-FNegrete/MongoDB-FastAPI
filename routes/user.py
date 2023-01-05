from fastapi import APIRouter
from config.db import conn
from schemas.user import userEntity, usersEntity

user = APIRouter()

@user.get('/users')
def find_all_users():
    return "hello world"

@user.post('/users')
def create_user():
    return "hello world"

@user.get('/users/{id}')
def find_user():
    return "hello world"

@user.put('/users/{id}')
def update_user():
    return "hello world"

@user.delete('/users/{id}')
def delete_user():
    return "hello world"

@user.get('/users')
def find_all_users():
    return "hello world"