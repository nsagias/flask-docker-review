# src/tests/test_users.py

import json
from src import db
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

    
def test_single_user(test_app, test_database):
    user = User(username='anyperson', email='anypersonemail@anywhere.com')
    db.session.add(user)
    db.session.commit()
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
    

