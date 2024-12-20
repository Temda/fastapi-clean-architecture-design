
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from src.repositories.user_repository import UserRepository
from src.services.user_service import UserService
from src.entities.user_entities import User
from src.config.database import SessionLocal, init_db
from src.entities.user_pydantic import UserCreate, UserResponse, UsersResponseAll 

app = FastAPI()

init_db()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_user_service(db: Session = Depends(get_db)):
    user_repository = UserRepository(db)
    return UserService(user_repository)

@app.get("/")
async def root():
    return {"message": "Hello, FastAPI with MySQL"}

@app.post("/user", response_model=UserResponse)
def create_user(user: UserCreate, user_service: UserService = Depends(get_user_service)):
    created_user = user_service.create_user(user)
    return created_user

@app.get("/users", response_model=UsersResponseAll)
def get_users(user_service: UserService = Depends(get_user_service)):
    users = user_service.get_user_all()
    if not users:
        raise HTTPException(status_code=404, detail="No users found")
    return {"data": users, "total": len(users)}

@app.get("/user/{user_id}", response_model=UserResponse)
def get_user(user_id: int, user_service: UserService = Depends(get_user_service)):
    user = user_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user