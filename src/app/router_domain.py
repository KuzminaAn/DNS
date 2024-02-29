from fastapi import APIRouter, Header, Path, Response

from src.app.schemas import CreateDomains
from src.db.functions import (
    create_domain,
    delete_domain,
    read_domain,
    update_domain,
)

router_domain = APIRouter(prefix="/domain", tags=["domain"])


# read domain
@router_domain.get("/{domain_id}")
async def read_d(domain_id: int = Path(ge=1)):
    result = read_domain(domain_id)
    if not result:
        return Response(status_code=404)
    return result


# create domain
@router_domain.post("/")
async def create_d(
    item: CreateDomains, user_id: int = Header(default=None, alias="X-User")
):
    result = create_domain(item.domain_name, user_id)
    return result


# curl -X POST http://127.0.0.1:7000/domain/ -H "X-User: 14" -H "Content-type: application/json" -d '{"domain_name": "This is my domain router"}'


# update domain
@router_domain.put("/{domain_id}")
async def update_d(item: CreateDomains, domain_id: int = Path(ge=1)):
    result = read_domain(domain_id)
    if not result:
        return Response(status_code=404)
    result = update_domain(item.domain_name, domain_id)
    return result


# curl -X PUT http://127.0.0.1:7000/domain/2  -H "Content-type: application/json" -d '{"domain_name": "NEWrouter"}'


# delete
@router_domain.delete("/{domain_id}")
async def delete_d(domain_id: int = Path(ge=1)):
    result = read_domain(domain_id)
    if not result:
        return Response(status_code=404)
    delete_domain(domain_id)
    return Response(status_code=204)


# curl -X DELETE http://127.0.0.1:7000/domain/3
