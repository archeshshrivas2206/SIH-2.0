from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
def test_posts():
    return {"message": "Posts router working!"}
