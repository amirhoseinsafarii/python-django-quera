from sqlalchemy import func, select, update, delete
from sqlalchemy.orm import Session

from models import Review


class ReviewManager:
    def __init__(self, session: Session):
        self.session = session

    def create(self, movie_id: int, user_id: int, rating: int, comment: str = None) -> Review:
        review = Review(movie_id=movie_id, user_id=user_id, rating=rating, comment=comment)
        self.session.add(review)
        self.session.commit()
        return review

    def get(self, review_id: int) -> Review | None:
        return self.session.get(Review, review_id)
        
    def get_all(self):
        return self.session.execute(select(Review)).scalars().all()

    def get_reviews_by_user(self, user_id: int):
        stmt = select(Review).where(Review.user_id == user_id)
        return self.session.execute(stmt).scalars().all()

    def get_latest_reviews_for_movie_by_time(self, movie_id: int, limit: int = 5):
        stmt= select(Review).where(Review.movie_id==movie_id).order_by(Review.created_at.desc()).limit(limit)
        return self.session.execute(stmt).scalars().all()

    def get_highest_rated_reviews(self, movie_id: int, limit: int = 5):
        stmt = select(Review).where(Review.movie_id==movie_id).order_by(Review.rating.desc()).limit(limit)
        return self.session.execute(stmt).scalars().all()

    def get_average_rating_by_user(self):
        stmt = select(
            Review.user_id,
            func.avg(Review.rating).label("average_rating")
        ).group_by(Review.user_id)
        return self.session.execute(stmt).all()

    def update(self, review_id: int, update_data: dict) -> Review:
        review = self.session.get(Review, review_id)

        if review is None:
            return None

        if "comment" in update_data:
            review.comment = update_data["comment"]

        if "rating" in update_data:
            review.rating = update_data["rating"]

        self.session.commit()
        return review

    def delete(self, review_id: int) -> bool:
        review = self.session.get(Review, review_id)
        if review:
            self.session.delete(review)
            self.session.commit()
            return True
        else:
            return False