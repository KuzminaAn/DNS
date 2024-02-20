from fastapi.testclient import TestClient
from src.app.main import app
from src.db.functions import read_domain, read_record


client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API LIVE!"}


def test_read_d_correct():
    domain_id = 2
    response = client.get(f"/domain/{domain_id}")
    assert response.status_code == 200
    assert response.json() == read_domain(domain_id).dict()


def test_read_d_error():
    domain_id = 200
    response = client.get(f"/domain/{domain_id}")
    assert response.status_code == 404


def test_create_domain():
    response = client.post("/domain", headers={"X-User": "11"}, json={"domain_name": "Test 20"})
    data = response.json()
    domain_id = data["domain_id"]
    assert response.status_code == 200
    assert response.json() == read_domain(domain_id).dict()


def test_update_domain_correct():
    domain_id = 10
    response = client.put(f"/domain/{domain_id}", json={"domain_name": "test21"})
    assert response.status_code == 200
    assert response.json() == read_domain(domain_id).dict()


def test_update_domain_error():
    domain_id = 150
    response = client.put(f"/domain/{domain_id}", json={"domain_name": "test1"})
    assert response.status_code == 404


def test_delete_correct():
    domain_id = 11
    response = client.delete(f"/domain/{domain_id}")
    assert response.status_code == 204


def test_delete_error():
    domain_id = 11
    response = client.delete(f"/domain/{domain_id}")
    assert response.status_code == 404


def test_read_r_correct():
    domain_id = 6
    response = client.get(f"/record/{domain_id}")
    assert response.status_code == 200
    assert len(response.json()) == len(read_record(domain_id))

    data1 = response.json()
    data2 = read_record(domain_id)
    for i in data2:
        assert i.dict() in data1


def test_read_r_error():
    domain_id = 600
    response = client.get(f"/record/{domain_id}")
    assert response.status_code == 404


def test_create_record():
    response = client.post("/record", json={"domain_id": 10, "record_type": "testA", "record": "test127.0.0.1", "ttl": 1010})
    data = response.json()
    domain_id = data["domain_id"]
    assert response.status_code == 200


def test_update_record_correct():
    record_id = 21
    response = client.put(f"/record/{record_id}", json={"domain_id": 10, "record_type": "test_updA", "record": "udateNEW", "ttl": 123})
    assert response.status_code == 200


def test_update_record_error():
    record_id = 222
    response = client.put(f"/record/{record_id}", json={"domain_id": 10, "record_type": "test_updA", "record": "udateNEW", "ttl": 123})
    assert response.status_code == 404

