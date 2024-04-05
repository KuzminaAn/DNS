from fastapi import APIRouter, Header, Path, Response

from src.schemas.schemas import CreateDomains
from src.db.functions import (
    create_domain,
    delete_domain,
    read_domain,
    read_domain_by_user_id,
    update_domain,
)

router_domain = APIRouter(prefix="/domain", tags=["domain"])

header = Header(default=None, alias="X-User", ge=1)


@router_domain.get("/{domain_id}")
async def read_d(domain_id: int = Path(ge=1)):
    result = read_domain(domain_id)
    if not result:
        return Response(status_code=404)
    return result


@router_domain.get("/")
async def read_by_user(user_id: int = header):
    result = read_domain_by_user_id(user_id)
    if not result:
        return Response(status_code=404)
    return result


@router_domain.post("/")
async def create_d(
    item: CreateDomains, user_id: int = Header(default=None, alias="X-User")
):
    result = create_domain(item.domain_name, user_id)
    return result


@router_domain.put("/{domain_id}")
async def update_d(item: CreateDomains, domain_id: int = Path(ge=1)):
    result = read_domain(domain_id)
    if not result:
        return Response(status_code=404)
    result = update_domain(item.domain_name, domain_id)
    return result


@router_domain.delete("/{domain_id}")
async def delete_d(domain_id: int = Path(ge=1)):
    result = read_domain(domain_id)
    if not result:
        return Response(status_code=404)
    delete_domain(domain_id)
    return Response(status_code=204)
