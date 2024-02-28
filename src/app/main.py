from fastapi import FastAPI
from src.app.router_domain import router_domain
from src.app.router_records import router_record


app = FastAPI()


app.include_router(router_domain)

app.include_router(router_record)


@app.get("/")
async def root():
    return {"message": "API LIVE!"}
