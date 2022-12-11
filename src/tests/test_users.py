# src/tests/test_users.py

import json
from src.api.models import User

def test_add_user(test_app, test_database):
    client = test_app.test_client()
    resp = client.post(
        '/users',
        data=json.dumps({
            'username' : 'nick',
            'email': 'anyemail@anywhere.com'
        }),
        content_type='application/json'
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 201
    assert 'anyemail@anywhere.com was added!' in data['message']

def test_add_user_invalid_json(test_app, test_database):
    client = test_app.test_client()
    resp = client.post(
        '/users',
        data=json.dumps({}),
        content_type='application/json',
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 400
    assert 'Input payload validation failed' in data['message']

def test_add_user_invalid_json_keys(test_app, test_database):
    client = test_app.test_client()
    resp = client.post(
        '/users',
        data=json.dumps({"email": "any@email.com"}),
        content_type='application/json',
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 400
    assert 'Input payload validation failed' in data['message']

def test_single_user(test_app, test_database, add_user):
    user = add_user('anyperson','anypersonemail@anywhere.com')
    client = test_app.test_client()
    resp = client.get(f'/users/{user.id}')
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert 'anyperson' in data['username']
    assert 'anypersonemail@anywhere.com' in data['email']

def test_single_user_incorrect_id(test_app, test_database):
    client = test_app.test_client()
    resp = client.get('/users/999')
    data = json.loads(resp.data.decode())
    assert resp.status_code == 404
    assert 'User 999 does not exist' in data['message']

def test_all_users(test_app, test_database, add_user):
    add_user('nick', 'nick@anyplace.com')
    add_user('nick2', 'nick2@anyplace.com')
    client = test_app.test_client()
    resp = client.get('/users')
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert len(data) == 2
    assert 'nick' in data[0]['username']
    assert 'nick@anyplace.com' in data[0]['email']
    assert 'nick2' in data[1]['username']
    assert 'nick2@anyplace.com' in data[1]['email']