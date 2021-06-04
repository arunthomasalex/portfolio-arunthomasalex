import json
import pytest

def test_add_message(client):
    message = {
        "name" : "test", 
        "email" : "testemail", 
        "subject" : "testsbject", 
        "message" : "testmessage"
    }
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'Accept': "application/json"
    }
    resp = client.post("/message/", data = message, headers = headers)
    assert resp.status_code == 201
    
def test_get_message_name(client):
    resp = client.get("/message/test")
    assert resp.status_code == 200

def test_delete_invalid_message(client):
    resp = client.delete(f"/message/0")
    assert resp.status_code == 204

def test_delete_message(client):
    resp = client.get("/message/test")
    json_data = json.loads(resp.data)[0]
    resp = client.delete(f"/message/{json_data['id']}")
    assert resp.status_code == 200
