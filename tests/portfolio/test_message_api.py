import json
import pytest

test_data = {
    "name" : "test_name", 
    "email" : "test_email@test.cmo", 
    "subject" : "tests_subject", 
    "message" : "test_message"
}

def test_post_message(client):
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'Accept': "application/json"
    }
    resp = client.post("/message", data = test_data, headers = headers)
    assert resp.status_code == 201

def test_get_all_messages(client):
    resp = client.get("/message")
    assert resp.status_code == 200

def test_get_all_message_name_filter(client):
    resp = client.get(f"/message?name={test_data['name']}")
    assert resp.status_code == 200
    json_data = json.loads(resp.data)
    assert json_data[0]["name"] == test_data["name"]

def test_get_all_message_email_filter(client):
    resp = client.get(f"/message?email={test_data['email']}")
    assert resp.status_code == 200
    json_data = json.loads(resp.data)
    assert json_data[0]["email"] == test_data["email"]

def test_get_all_message_subject_filter(client):
    resp = client.get(f"/message?subject={test_data['subject']}")
    assert resp.status_code == 200
    json_data = json.loads(resp.data)
    assert json_data[0]["subject"] == test_data["subject"]

def test_get_message_by_id(client):
    resp = client.get("/message/1")
    assert resp.status_code == 200

def test_delete_message_by_id(client):
    resp = client.get("/message")
    json_data = json.loads(resp.data)
    json_data =json_data[len(json_data) - 1]
    resp = client.delete(f"/message/{json_data['id']}")
    assert resp.status_code == 200

def test_invalid_delete_message_by_id(client):
    resp = client.delete(f"/message/0")
    assert resp.status_code == 204