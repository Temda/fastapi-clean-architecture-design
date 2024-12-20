from sqlalchemy.future import select
from src.entities.user_entities import User

class UserRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    def save(self, user: User):
        self.db_session.add(user)
        self.db_session.commit()
        self.db_session.refresh(user)
        return user

    def find_all_users(self):
        result = self.db_session.query(User).all()
        return result

    def find_by_id(self, user_id: int):
        return self.db_session.query(User).filter(User.user_id == user_id).first()
