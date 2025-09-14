from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
def test_alumni():
    return {"message": "Alumni router working!"}
