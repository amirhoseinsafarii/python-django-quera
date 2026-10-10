from datetime import datetime
from sqlalchemy import select, func, update, delete
from sqlalchemy.orm import Session

from models import Movie, Genre, Review, MovieGenre


class MovieManager:
    def __init__(self, session: Session) -> None:
        self.session = session

    def create(self, title: str, release_year: int) -> Movie:
        movie = Movie(title=title, release_year=release_year)
        self.session.add(movie)
        self.session.commit()
        return movie

    def get(self, movie_id: int) -> Movie | None:
        return self.session.get(Movie, movie_id)

    def get_all(self):
        return self.session.execute(select(Movie)).scalars().all()

    def add_genre(self, movie_id: int, genre: Genre) -> Movie:
        movie = self.session.get(Movie, movie_id)
        movie.genres.append(genre)
        self.session.commit()
        return movie

    def get_reviews(self, movie_id: int):
        movie = self.session.get(Movie, movie_id)
        return movie.reviews if movie is not None else None

    def get_average_rating(self, movie_id: int):
        result = self.session.query(
            func.avg(Review.rating)
            ).filter(Review.movie_id==movie_id
                     ).scalar()
        return float(result) if result is not None else None

    def update(self, movie_id: int, update_data: dict) -> Movie:
        stmt = (
            update(Movie)
            .where(Movie.id == movie_id)
            .values(title=update_data.get("title"),
            release_year=update_data.get("release_year"))
            .returning(Movie)
        )
        movie = self.session.execute(stmt).scalar_one_or_none()
        self.session.commit()
        return movie
    
    def delete(self, movie_id: int) -> bool:
        movie = self.session.get(Movie, movie_id)
        if movie:
            self.session.delete(movie)
            self.session.commit()
            return True
        else:
            return False

    def remove_genre(self, movie_id: int, genre: Genre) -> Movie | None:
        stmt = delete(MovieGenre).where(
            MovieGenre.movie_id == movie_id,
            MovieGenre.genre_id == genre.id
        )
        self.session.execute(stmt)
        self.session.commit()

        return self.session.get(Movie, movie_id)

    def get_top_movies_by_rating(self, limit: int = 10) -> list[tuple]:
        stmt = select(
            Movie,
            func.avg(Review.rating).label("average_rating")
            ).join(Review, Review.movie_id == Movie.id).group_by(Movie.id).order_by(func.avg(Review.rating).desc()).limit(limit)
        
        return self.session.execute(stmt).all()
        

    def get_movies_by_genre(self, genre_name: str) -> list[Movie]:
        stmt = select(Movie).join(Movie.genres).where(Genre.name==genre_name)
        return self.session.execute(stmt).scalars().all()

    def get_top_rated_movies_by_genre(self) -> list[tuple]:
        stmt = (
            select(
                Genre.name,
                Movie.title,
                func.avg(Review.rating).label("average_rating")
            )
            .join(MovieGenre, Genre.id == MovieGenre.genre_id)
            .join(Movie, Movie.id == MovieGenre.movie_id)
            .join(Review, Review.movie_id == Movie.id)
            .group_by(Genre.id, Genre.name, Movie.id, Movie.title)
            .order_by(Genre.name, func.avg(Review.rating).desc())
        )

        return self.session.execute(stmt).all()

    # def get_top_rated_movies_by_genre(self):
    #     stmt = select(
    #         Genre.name,
    #         Movie.titl,
    #         func.avg(Review.rating).label("average_rating")
    #     ).join(Movie.genres
    #         ).join(
    #             Review, Review.movie_id == Movie.id
    #         ).group_by(
    #             Genre.name, Movie.id, Movie.title
    #         ).order_by(Genre.name, func.avg(Review.rating).desc())
    #     return self.session.execute(stmt).all()