from sqlalchemy import select, update, delete, func
from sqlalchemy.orm import Session

from models import Genre, Movie, MovieGenre


class GenreManager:
    def __init__(self, session: Session):
        self.session = session

    def create(self, name: str) -> Genre:
        genre = Genre(name=name)
        self.session.add(genre)
        self.session.commit()
        return genre
        
    def get(self, genre_id: int) -> Genre | None:
        return self.session.get(Genre, genre_id)

    def get_all(self):
        return self.session.execute(select(Genre)).scalars().all()

    def get_genre_by_name(self, name: str) -> Genre | None:
        return self.session.execute(select(Genre).where(Genre.name==name)).scalar_one_or_none()


    def update(self, genre_id: int, new_name: str) -> Genre:
        stmt = update(Genre).where(Genre.id==genre_id).values(name=new_name).returning(Genre)
        genre = self.session.execute(stmt).scalar_one_or_none()
        self.session.commit()
        return genre

    def delete(self, genre_id: int) -> bool:
        genre = self.session.get(Genre, genre_id)
        if genre:
            self.session.delete(genre)
            self.session.commit()
            return True
        else:
            return False
        

    def get_genres_with_most_movies(self) -> list[tuple]:
        stmt = (
            select(Genre, func.count(MovieGenre.movie_id).label("movie_count"))
            .join(MovieGenre, Genre.id == MovieGenre.genre_id)
            .group_by(Genre.id)
            .order_by(func.count(MovieGenre.movie_id).desc())
        )

        return self.session.execute(stmt).all()