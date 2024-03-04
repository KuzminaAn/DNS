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
def fixture_test_delete_correct():
    domain_id = 5
    return domain_id


@pytest.fixture
def fixture_test_delete_error():
    domain_id = 5
    return domain_id


@pytest.fixture
def fixture_test_read_r_correct():
    domain_id = 4
    return domain_id


@pytest.fixture
def fixture_test_read_r_error():
    domain_id = 600
    return domain_id


@pytest.fixture
def fixture_test_update_record_correct():
    record_id = 5
    return record_id


@pytest.fixture
def fixture_test_update_record_error():
    record_id = 90
    return record_id
