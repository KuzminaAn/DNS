from sqlalchemy import delete, select, update

from src.db.session import session_scope
from src.db.table import Records, Users


def read_domain(domain_id: int):
    stmt = select(Users).where(Users.domain_id == domain_id)
    with session_scope() as s:
        result = s.execute(stmt).scalar()
    return result


def read_domain_by_user_id(user_id: int):
    stmt = select(Users).where(Users.user_id == user_id)
    with session_scope() as s:
        result = s.execute(stmt).scalars().all()
    return result


def create_domain(domain_name: str, user_id: int):
    domain = Users(user_id=user_id, domain_name=domain_name)
    with session_scope() as s:
        s.add(domain)
        s.flush()
        result = s.execute(
            select(Users).where(Users.domain_id == domain.domain_id)
        ).scalar()
    return result


def update_domain(domain_name: str, domain_id: int):
    stmt = (
        update(Users)
        .values(domain_name=domain_name)
        .where(Users.domain_id == domain_id)
    )
    with session_scope() as s:
        s.execute(stmt)
    return read_domain(domain_id)


def delete_domain(domain_id: int):
    stmt = delete(Users).where(Users.domain_id == domain_id)
    with session_scope() as s:
        result = s.execute(stmt)
    return result


def read_record(domain_id: int):
    stmt = select(Records).where(Records.domain_id == domain_id)
    with session_scope() as s:
        result = s.execute(stmt).scalars().all()
    return result


def create_record(domain_id: int, record_type: str, record: str, ttl: int):
    record = Records(
        domain_id=domain_id, record_type=record_type, record=record, ttl=ttl
    )
    with session_scope() as s:
        s.add(record)
        s.flush()
        s.commit()
    return record


def read_record_by_record_id(domain_id: int, record_id: int):
    stmt = select(Records).where(Records.domain_id == domain_id, Records.record_id == record_id)
    with session_scope() as s:
        result = s.execute(stmt).scalar()
    return result


def update_record(
    domain_id: int, record_type: str, record: str, ttl: int, record_id: int
):
    stmt = (
        update(Records)
        .values(
            record_type=record_type,
            record=record,
            ttl=ttl,
        )
        .where(Records.domain_id == domain_id, Records.record_id == record_id)
    )
    with session_scope() as s:
        s.execute(stmt)
    return read_record_by_record_id(domain_id, record_id)


def delete_domain(domain_id: int):
    stmt = delete(Users).where(Users.domain_id == domain_id)
    with session_scope() as s:
        result = s.execute(stmt)
    return result


def delete_record(domain_id: int, record_id: int):
    stmt = delete(Records).where(Records.domain_id == domain_id, Records.record_id == record_id)
    with session_scope() as s:
        result = s.execute(stmt)
    return result
