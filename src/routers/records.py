from fastapi import APIRouter, Path, Response

from src.schemas.schemas import CreateRecords
from src.db.functions import (
    create_record,
    delete_record,
    read_record,
    read_record_by_record_id,
    update_record,
)

router_record = APIRouter(prefix="/domain", tags=["record"])


@router_record.get("/{domain_id}/record")
async def read_r(domain_id: int = Path(ge=1)):
    result = read_record(domain_id)
    if not result:
        return Response(status_code=404)
    return result


@router_record.get("/{domain_id}/record/{record_id}")
async def read_r_by_record_id(domain_id: int = Path(ge=1), record_id: int = Path(ge=1)):
    result = read_record_by_record_id(domain_id, record_id)
    if not result:
        return Response(status_code=404)
    return result


@router_record.post("/{domain_id}/record")
async def create_r(item: CreateRecords, domain_id: int = Path(ge=1)):
    result = create_record(
        domain_id, item.record_type, item.record, item.ttl
    )
    return result


@router_record.put("/{domain_id}/record/{record_id}")
async def update_r(item: CreateRecords, domain_id: int = Path(ge=1), record_id: int = Path(ge=1)):
    result = read_record_by_record_id(domain_id, record_id)
    if not result:
        return Response(status_code=404)
    result = update_record(
        domain_id, item.record_type, item.record, item.ttl, record_id
    )
    return result


@router_record.delete("/{domain_id}/record/{record_id}")
async def delete_r(domain_id: int = Path(ge=1), record_id: int = Path(ge=1)):
    result = read_record_by_record_id(domain_id, record_id)
    if not result:
        return Response(status_code=404)
    delete_record(domain_id, record_id)
    return Response(status_code=204)
