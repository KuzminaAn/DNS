from fastapi import APIRouter, Response, Path
from src.db.functions import create_record, read_record, update_record, read_record_by_record
from src.app.schemas import CreateRecords

router_record = APIRouter(prefix="/record", tags=["record"])


@router_record.get("/{domain_id}")
async def read_r(domain_id: int = Path(ge=1)):
    result = read_record(domain_id)
    if not result:
        return Response(status_code=404)
    return result


#create records
@router_record.post("/")
async def create_r(item: CreateRecords):
    result = create_record(item.domain_id, item.record_type, item.record, item.ttl)
    return result

#curl -X POST http://127.0.0.1:7000/record/ -H "Content-type: application/json" -d '{"domain_id": 6, "record_type": "Router", "record": "127.0.0.9", "ttl": 12345}'


#update record
@router_record.put("/{record_id}")
async def update_r(item: CreateRecords, record_id: int = Path(ge=1)):
    result = read_record_by_record(record_id)
    if not result:
        return Response(status_code=404)
    result = update_record(item.domain_id, item.record_type, item.record, item.ttl, record_id)
    return result

#curl -X PUT http://127.0.0.1:7000/record/17  -H "Content-type: application/json" -d '{"domain_id": 6, "record_type": "AA", "record": "NEW", "ttl": 12355}'
