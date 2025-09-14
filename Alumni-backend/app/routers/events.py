from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
def test_events():
    return {"message": "Events router working!"}
