from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
def test_chatbot():
    return {"message": "Chatbot router working!"}
