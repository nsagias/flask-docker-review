# src/tests/test_users.py

import json

def test_add_user(test_app, test_database):
    client = test_app.test_client()
    resp = client.post(
        '/users',
        data=json.dumps({
        'username' : 'nick',
        'email': 'anyemail@anywhere.com'
        }),
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 201
    assert 'anyemail@anywhere.com was added!' in data['message']
    
  