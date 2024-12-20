from src.repositories.user_repository import UserRepository
from src.entities.user_entities import User
from src.entities.user_pydantic import UserCreate

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, user: UserCreate):
        user_entity = User(name=user.name, is_active=user.is_active)
        return self.user_repository.save(user_entity)
    
    def get_user_all(self):
        result = self.user_repository.find_all_users()
        return result

    def get_user_by_id(self, user_id: int):
        return self.user_repository.find_by_id(user_id)