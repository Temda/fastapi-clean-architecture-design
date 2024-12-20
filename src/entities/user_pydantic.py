from typing import List
from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str 
    is_active: bool = False

class UserResponse(BaseModel):
    user_id: int
    name: str
    is_active: bool
    
    class Config:
        from_attributes = True

class UsersResponseAll(BaseModel):
    data: List[UserResponse]
    total: int