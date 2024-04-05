from fastapi import APIRouter

router_live = APIRouter(prefix="/liveness", tags=["live"])


@router_live.get("/")
async def root():
    return {"message": "API LIVE!"}
