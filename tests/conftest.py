import pytest


@pytest.fixture
def fixture_test_read_d_correct():
    domain_id = 2
    return domain_id


@pytest.fixture
def fixture_test_read_d_error():
    domain_id = 200
    return domain_id


@pytest.fixture
def fixture_test_update_domain_correct():
    domain_id = 4
    return domain_id


@pytest.fixture
def fixture_test_update_domain_error():
    domain_id = 101
    return domain_id


@pytest.fixture
def fixture_test_delete_domain_correct():
    domain_id = 5
    return domain_id


@pytest.fixture
def fixture_test_delete_domain_error():
    domain_id = 5
    return domain_id


@pytest.fixture
def fixture_test_read_r_correct():
    domain_id = 2
    return domain_id


@pytest.fixture
def fixture_test_read_r_error():
    domain_id = 200
    return domain_id


@pytest.fixture
def fixture_test_read_r_by_record_id_correct():
    domain_id = 2
    record_id = 9
    return domain_id, record_id


@pytest.fixture
def fixture_test_read_by_record_id_error():
    domain_id = 10
    record_id = 1
    return domain_id, record_id


@pytest.fixture
def fixture_test_create_record():
    domain_id = 3
    return domain_id


@pytest.fixture
def fixture_test_update_record_correct():
    domain_id = 1
    record_id = 6
    return domain_id, record_id


@pytest.fixture
def fixture_test_update_record_error():
    domain_id = 22
    record_id = 90
    return domain_id, record_id


@pytest.fixture
def fixture_test_delete_record_correct():
    domain_id = 2
    record_id = 3
    return domain_id, record_id


@pytest.fixture
def fixture_test_delete_record_error():
    domain_id = 2
    record_id = 12
    return domain_id, record_id
