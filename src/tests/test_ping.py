# src/tests/test_ping.py

import json

def test_ping(test_app):
  """
  GIVEN testing ping endpoint on docker/flask
  WHEN the ping enpoint is called and response is convert from json to dict
  THEN 
    check response code is '200'
    check response key 'messag' is value 'pong'
    check response key 'status' is value 'success'
  """
  # Given
  client = test_app.test_client()
  
  # When
  resp = client.get('/ping')
  data = json.loads(resp.data.decode())
  
  # Then
  assert resp.status_code == 200
  assert 'pong' in data['message']
  assert 'success' in data['status']