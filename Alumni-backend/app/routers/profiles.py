from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

# Fake DB for now
profiles_db = []

# Pydantic model for Profile
class Profile(BaseModel):
    id: int
    name: str
    email: str
    batch: Optional[str] = None
    course: Optional[str] = None
    company: Optional[str] = None
    position: Optional[str] = None

# Get all profiles
@router.get("/", response_model=List[Profile])
def get_profiles():
    return profiles_db

# Get a single profile by ID
@router.get("/{profile_id}", response_model=Profile)
def get_profile(profile_id: int):
    for profile in profiles_db:
        if profile.id == profile_id:
            return profile
    raise HTTPException(status_code=404, detail="Profile not found")

# Create a new profile
@router.post("/", response_model=Profile)
def create_profile(profile: Profile):
    for p in profiles_db:
        if p.id == profile.id:
            raise HTTPException(status_code=400, detail="Profile with this ID already exists")
    profiles_db.append(profile)
    return profile

# Update an existing profile
@router.put("/{profile_id}", response_model=Profile)
def update_profile(profile_id: int, updated_profile: Profile):
    for index, profile in enumerate(profiles_db):
        if profile.id == profile_id:
            profiles_db[index] = updated_profile
            return updated_profile
    raise HTTPException(status_code=404, detail="Profile not found")

# Delete a profile
@router.delete("/{profile_id}")
def delete_profile(profile_id: int):
    for index, profile in enumerate(profiles_db):
        if profile.id == profile_id:
            profiles_db.pop(index)
            return {"message": "Profile deleted successfully"}
    raise HTTPException(status_code=404, detail="Profile not found")
