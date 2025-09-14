from fastapi import FastAPI
from app.routers import auth, profiles, posts, events, chatbot
from app.routers import profiles
from fastapi.middleware.cors import CORSMiddleware




# Create FastAPI instance
app = FastAPI(
    title="Alumni Data Platform",
    description="Backend API for Alumni Management and Engagement",
    version="1.0.0"
)
app.include_router(profiles.router, prefix="/profiles", tags=["Profiles"])
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # later restrict to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(profiles.router, prefix="/profiles", tags=["Profiles"])
app.include_router(posts.router, prefix="/posts", tags=["Posts"])
app.include_router(events.router, prefix="/events", tags=["Events"])
app.include_router(chatbot.router, prefix="/chatbot", tags=["Chatbot"])

# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to Alumni Data Platform API 🚀"}
