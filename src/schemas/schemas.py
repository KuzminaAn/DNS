from pydantic import BaseModel, Field


class CreateDomains(BaseModel):
    domain_name: str = Field(min_length=1)


class CreateRecords(BaseModel):
    record_type: str = Field(min_length=1)
    record: str = Field(min_length=1)
    ttl: int
