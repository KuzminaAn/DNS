from table import Users, Records
from session import session_scope
from sqlalchemy import select


# обновить домен
# def update_domain(domain_name:str, domain_id: int):
#    stmt = (
#        update(Users)
#        .values(.......)
#        .where(Users.domain_id == domain_id)


# обновить запись
# def update_record(type:str, record:str, TTL, record_id: int):
#    stmt = (
#        update(Records)
#        .values(........)
#        .where(Records.record_id == record_id)
#    )


# удалить домен
# def delete_domain(domain_id:int):
#    stmt = delete(Users).where(Users.domain_id == domain_id)
#    with session_scope() as s:
#        result = s.execute(stmt)
#    return result


# создать домен
def create_domain(domain_name: str, user_id: int):
    domain = Users(
        user_id=user_id,
        domain_name=domain_name
    )
    with session_scope() as s:
        s.add(domain)
        s.flush()
        result = s.execute(select(Users).where(Users.domain_id == domain.domain_id)).scalar()
    return result


# создать запись
def create_record(domain_id: int, record_type: str, record: str, ttl: int):
    record = Records(
        domain_id=domain_id,
        record_type=record_type,
        record=record,
        ttl=ttl
    )
    with session_scope() as s:
        s.add(record)
        s.flush()
        result = s.execute(select(Records).where(Records.record_id == record.record_id))
    return result





# read

#def reade_table(domain_id:int):
#    stmt = select(Users).where(Users.domain_id == domain_id)
#    with session_scope() as s:
#        query = s.query(Users, Records).filter(Users.domain_id == Records.domain_id).all()
#    return query


def read_t(domain_id: int):
    stmt = select(Users, Records).where(Users.domain_id == domain_id, Records.domain_id == domain_id)
    with session_scope() as s:
        result = s.execute(stmt).all
    return result


#def read_id(domain_id: int):
#    stmt = select(Users).where(Users.domain_id == domain_id)
#    with session_scope() as s:
#        result = s.execute(stmt).scalar()
#    return result
