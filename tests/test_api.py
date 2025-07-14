from fastapi.testclient import TestClient

from main import app
from src.db.functions import read_domain, read_domain_by_user_id, read_record, read_record_by_record_id
from tests.test_vars import VariableDomain, VariableRecord

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API LIVE!"}


def test_read_d_correct(fixture_test_read_d_correct):
    domain_id = fixture_test_read_d_correct
    response = client.get(f"/domain/{domain_id}")
    assert response.status_code == 200
    assert response.json() == read_domain(domain_id).dict()


def test_read_d_error(fixture_test_read_d_error):
    domain_id = fixture_test_read_d_error
    response = client.get(f"/domain/{domain_id}")
    assert response.status_code == 404


def test_read_by_user_id_correct(fixture_test_read_by_user_id_correct):
    user_id = fixture_test_read_by_user_id_correct
    response = client.get("/domain/", headers={"X-User": str(user_id)})
    assert response.status_code == 200
    assert len(response.json()) == len(read_domain_by_user_id(user_id))

    data1 = response.json()
    data2 = read_domain_by_user_id(user_id)
    for i in data2:
        assert i.dict() in data1


def test_read_by_user_id_error(fixture_test_read_by_user_id_error):
    user_id = fixture_test_read_by_user_id_error
    response = client.get("/domain/", headers={"X-User": str(user_id)})
    assert response.status_code == 404


def test_create_domain():
    response = client.post(
        "/domain",
        headers=VariableDomain.header_create_domain,
        json=VariableDomain.json_create_domain,
    )
    data = response.json()
    domain_id = data["domain_id"]
    assert response.status_code == 200
    assert response.json() == read_domain(domain_id).dict()


def test_update_domain_correct(fixture_test_update_domain_correct):
    domain_id = fixture_test_update_domain_correct
    response = client.put(
        f"/domain/{domain_id}", json=VariableDomain.json_update_domain_correct
    )
    assert response.status_code == 200
    assert response.json() == read_domain(domain_id).dict()


def test_update_domain_error(fixture_test_update_domain_error):
    domain_id = fixture_test_update_domain_error
    response = client.put(
        f"/domain/{domain_id}", json=VariableDomain.json_update_domain_error
    )
    assert response.status_code == 404


def test_delete_domain_correct(fixture_test_delete_domain_correct):
    domain_id = fixture_test_delete_domain_correct
    response = client.delete(f"/domain/{domain_id}")
    assert response.status_code == 204


def test_delete_error(fixture_test_delete_domain_error):
    domain_id = fixture_test_delete_domain_error
    response = client.delete(f"/domain/{domain_id}")
    assert response.status_code == 404


def test_read_r_correct(fixture_test_read_r_correct):
    domain_id = fixture_test_read_r_correct
    response = client.get(f"/domain/{domain_id}/record")
    assert response.status_code == 200
    assert len(response.json()) == len(read_record(domain_id))

    data1 = response.json()
    data2 = read_record(domain_id)
    for i in data2:
        assert i.dict() in data1


def test_read_r_error(fixture_test_read_r_error):
    domain_id = fixture_test_read_r_error
    response = client.get(f"/domain/{domain_id}/record")
    assert response.status_code == 404


def test_read_r_by_record_id_correct(fixture_test_read_r_by_record_id_correct):
    domain_id, record_id = fixture_test_read_r_by_record_id_correct
    response = client.get(f"/domain/{domain_id}/record/{record_id}")
    assert response.status_code == 200
    assert response.json() == read_record_by_record_id(domain_id, record_id).dict()


def test_read_r_by_record_id_error(fixture_test_read_by_record_id_error):
    domain_id, record_id = fixture_test_read_by_record_id_error
    response = client.get(f"/domain/{domain_id}/record/{record_id}")
    assert response.status_code == 404


def test_create_record(fixture_test_create_record):
    domain_id = fixture_test_create_record
    response = client.post(f"/domain/{domain_id}/record", json=VariableRecord.json_create_record)
    data = response.json()
    record_id = data["record_id"]
    assert response.status_code == 200
    assert response.json() == read_record_by_record_id(domain_id, record_id).dict()


def test_update_record_correct(fixture_test_update_record_correct):
    domain_id, record_id = fixture_test_update_record_correct
    response = client.put(
        f"/domain/{domain_id}/record/{record_id}", json=VariableRecord.json_update_record_correct
    )
    assert response.status_code == 200
    assert response.json() == read_record_by_record_id(domain_id, record_id).dict()


def test_update_record_error(fixture_test_update_record_error):
    domain_id, record_id = fixture_test_update_record_error
    response = client.put(
        f"/domain/{domain_id}/record/{record_id}", json=VariableRecord.json_update_record_error
    )
    assert response.status_code == 404


def test_delete_record_correct(fixture_test_delete_record_correct):
    domain_id, record_id = fixture_test_delete_record_correct
    response = client.delete(f"/domain/{domain_id}/record/{record_id}")
    assert response.status_code == 204


def test_delete_record_error(fixture_test_delete_record_error):
    domain_id, record_id = fixture_test_delete_record_error
    response = client.delete(f"/domain/{domain_id}/record/{record_id}")
    assert response.status_code == 404
