from sqlalchemy import func, select, update, delete
from sqlalchemy.orm import Session

from models import Review, User


class UserManager:
    def __init__(self, session: Session):
        self.session = session

    def create(self, name: str, email: str) -> User:
        user = User(name=name, email=email)
        self.session.add(user)
        self.session.commit()
        return user

    def get(self, user_id: int) -> User | None:
        return self.session.get(User, user_id)

    def get_all(self):
        return self.session.execute(select(User)).scalars().all()
        
    def get_user_by_email(self, email: str) -> User | None:
        return self.session.execute(select(User).where(User.email==email)).scalar_one_or_none()

    def get_most_active_users(self, limit=5):
        stmt = (
            select(
                User.id,
                func.count(Review.id).label('review_count')
            ).join(User.reviews
                ).group_by(User.id
                ).order_by(func.count(Review.id).label('review_count').desc()
                ).limit(limit)
            )
        return self.session.execute(stmt).all()

    def update(self, user_id: int, update_data: dict) -> User | None:
        user = self.session.get(User, user_id)

        if user is None:
            return None

        if "name" in update_data:
            user.name = update_data["name"]

        if "email" in update_data:
            user.email = update_data["email"]

        if "is_verified" in update_data:
            user.is_verified = update_data["is_verified"]

        self.session.commit()
        return user

    def delete(self, user_id: int) -> bool:
        user = self.session.get(User, user_id)
        if user:
            self.session.delete(user)
            self.session.commit()
            return True
        else:
            return False

    def verify_user(self, user_id: int) -> User:
        stmt = update(User).where(User.id==user_id).values(is_verified=True).returning(User)
        result = self.session.execute(stmt)
        return result.scalar_one_or_none()