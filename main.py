from fastapi import FastAPI, Response, Header
from pydantic import BaseModel, Field
from functions import read_domain, create_domain, create_record, update_domain, read_record, update_record, delete_domain, read_record_by_record


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Helllllo"}


# read domain
@app.get("/domain/{domain_id}")
async def read_d(domain_id: int):
    result = read_domain(domain_id)
    if not result:
        return Response(status_code=404)
    return result


class CreateItem(BaseModel):
    domain_name: str = Field(min_length=1)


#create domain
@app.post("/domain")
async def create_d(item: CreateItem, user_id: int = Header(default=None, alias="X-User")):
    result = create_domain(item.domain_name, user_id)
    return result

#curl -X POST http://127.0.0.1:7000/domain -H "X-User: 5" -H "Content-type: application/json" -d '{"domain_name": "This is my domain44"}'


#update domain
@app.put("/domain/{domain_id}")
async def update_d(item: CreateItem, domain_id: int):
    result = read_d(domain_id)
    if not result:
        return Response(status_code=404)
    result = update_domain(item.domain_name, domain_id)
    return result

#curl -X PUT http://127.0.0.1:7000/domain/1  -H "Content-type: application/json" -d '{"domain_name": "NEW2"}'


#delete
@app.delete("/domain/{domain_id}")
async def delete_d(domain_id: int):
    result = read_domain(domain_id)
    if not result:
        return Response(status_code=404)
    delete_domain(domain_id)
    return Response(status_code=204)

#curl -X DELETE http://127.0.0.1:7000/domain/3


@app.get("/record/{domain_id}")
async def read_r(domain_id: int):
    result = read_record(domain_id)
    if not result:
        return Response(status_code=404)
    return result


class CreateRecords(BaseModel):
    domain_id: int
    record_type: str = Field(min_length=1)
    record: str = Field(min_length=1)
    ttl: int


#create records
@app.post("/record")
async def create_r(item: CreateRecords):
    result = create_record(item.domain_id, item.record_type, item.record, item.ttl)
    return result


#curl -X POST http://127.0.0.1:7000/record -H "Content-type: application/json" -d '{"domain_id": 5, "record_type": "A12", "record": "127.0.0.1", "ttl": 1234}'


#update record

@app.put("/record/{record_id}")
async def update_r(item: CreateRecords, record_id: int):
    result = read_record_by_record(record_id)
    if not result:
        return Response(status_code=404)
    result = update_record(item.domain_id, item.record_type, item.record, item.ttl, record_id)
    return result

#curl -X PUT http://127.0.0.1:7000/record/8  -H "Content-type: application/json" -d '{"domain_id": 1, "record_type": "AA", "record": "NEW", "ttl": 123}'


