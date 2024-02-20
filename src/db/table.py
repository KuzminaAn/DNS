from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declared_attr

Base = declarative_base()


class Users(Base):
    __tablename__ = "users"

    domain_id = Column("domain_id", Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    user_id = Column("user_id", Integer, nullable=False, unique=True, primary_key=True)
    domain_name = Column("domain_name", String, nullable=False, unique=True)

    def __init__(self, user_id: int, domain_name: str):
        self.user_id = user_id
        self.domain_name = domain_name

    def dict(self):
        return dict(
            domain_id=self.domain_id,
            user_id=self.user_id,
            domain_name=self.domain_name
        )


class Records(Base):
    __tablename__ = "records"

    record_id = Column("record_id", Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    record_type = Column("record_type", String, nullable=False)
    record = Column("record", String, nullable=False)
    ttl = Column("ttl", Integer, nullable=False)

    @declared_attr
    def domain_id(self):
        return Column(
            Integer,
            ForeignKey("users.domain_id", ondelete="CASCADE"),
            nullable=False,
        )

    def __int__(self, domain_id: int, record_type: str, record: str, ttl: int):
        self.domain_id = domain_id
        self.record_type = type
        self.record = record
        self.ttl = ttl

    def dict(self):
        return dict(
            record_id=self.record_id,
            domain_id=self.domain_id,
            record_type=self.record_type,
            record=self.record,
            ttl=self.ttl
        )


