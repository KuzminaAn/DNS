class VariableDomain:
    header_create_domain = {"X-User": "20"}
    json_create_domain = {"domain_name": "Test 29.02"}
    json_update_domain_correct = {"domain_name": "testcorrect"}
    json_update_domain_error = {"domain_name": "testerror"}


class VariableRecord:
    json_create_record = {"domain_id": 4, "record_type": "test29", "record": "test127.0.0.1", "ttl": 100}
    json_update_record_correct = {"domain_id": 4, "record_type": "test29", "record": "udateNEW", "ttl": 123}
    json_update_record_error = {"domain_id": 10, "record_type": "test_updA", "record": "udateNEW", "ttl": 123}
