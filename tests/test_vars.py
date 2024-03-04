class VariableDomain:
    header_create_domain = {"X-User": "20"}
    json_create_domain = {"domain_name": "Test create 04.03"}
    json_update_domain_correct = {"domain_name": "test update 04.03"}
    json_update_domain_error = {"domain_name": "test update error"}


class VariableRecord:
    json_create_record = {
        "domain_id": 1,
        "record_type": "test create 04/03",
        "record": "127.0.0.1",
        "ttl": 100,
    }
    json_update_record_correct = {
        "domain_id": 2,
        "record_type": "test update 04/03",
        "record": "update NEW",
        "ttl": 123,
    }
    json_update_record_error = {
        "domain_id": 10,
        "record_type": "test update error 04/03",
        "record": "update NEW",
        "ttl": 123,
    }
