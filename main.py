from fastapi import FastAPI, Response, Header
from functions import read_t
from pydantic import BaseModel, Field
from functions import create_domain, create_record



app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Helllllo"}


# read
@app.get("/domain_id")
async def read_t(domain_id: int):
    result = read_t(domain_id)
    if not result:
        return Response(status_code=404)
    return result


class CreateItem(BaseModel):
    domain_name: str = Field(min_length=1)


#create
@app.post("/name")
async def create_d(item: CreateItem, user_id: int = Header(default=None, alias="X-User")):
    result = create_domain(item.domain_name, user_id)
    return result

#curl -X POST http://127.0.0.1:7000/name -H "X-User: 1" -H "Content-type: application/json" -d '{"domain_name": "This is my domain"}'

#curl -X POST http://localhost:7000/name -H "X-User: 1" -H "Content-type: application/json" -d '{"domain_name": "This is my domain"}'


class CreateRecords(BaseModel):
    domain_id: int
    record_type: str = Field(min_length=1)
    record: str = Field(min_length=1)
    ttl: int


#create records
@app.post("/record")
async def create_r(item: CreateRecords):
    result = create_record(item.record_type, item.record, item.ttl, item.domain_id)
    return result


#curl -X POST http://127.0.0.1:7000/record -H "Content-type: application/json" -d '{"domain_id": "1", "record_type": "A", "record": "0.0.0.0", "ttl": "1234"}'