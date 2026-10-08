from sqlalchemy import func, select
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