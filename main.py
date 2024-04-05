from fastapi import FastAPI

from src.routers.liveness import router_live
from src.routers.domains import router_domain
from src.routers.records import router_record

app = FastAPI()


app.include_router(router_live)

app.include_router(router_domain)

app.include_router(router_record)
