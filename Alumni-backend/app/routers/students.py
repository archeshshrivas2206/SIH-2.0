from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
def test_students():
    return {"message": "Students router working!"}
