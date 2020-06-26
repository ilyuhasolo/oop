import psycopg2
from User import User
from Anime import Anime
from Author import Author
from Studio import Studio
from Review import Review


class DataBase:
    _db = None
    _cur = None

    def __init__(self, dbname: str, dpassword: str):
        self._db = psycopg2.connect(
            database=dbname,
            user="postgres",
            password=dpassword,
            host="localhost",
            port="5432"
        )
        self._cur = self._db.cursor()

    def AddUser(self, user: User):
        request = "INSERT INTO person (nickname, login, password, avatar, about_yourself, registration_date)" \
                  "VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(
            user.GetNickname(),
            user.GetLogin(),
            user.GetPassword(),
            user.GetAvatar(),
            user.GetAboutYourself(),
            user.GetRegistrationDate())
        self._cur.execute(request)
        self._db.commit()

    def AddAnime(self, anime: Anime):
        request = "INSERT INTO anime (title, year, author_id, studio_id, format, description, poster)" \
                  "VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
            anime.GetTitle(),
            anime.GetYear(),
            anime.GetAuthorId(),
            anime.GetStudioId(),
            anime.GetFormat(),
            anime.GetDescription(),
            anime.GetPoster())
        self._cur.execute(request)
        self._db.commit()

    def AddStudio(self, studio: Studio):
        request = "INSERT INTO studio (name, logo, description)" \
                  "VALUES ('{}', '{}', '{}')".format(
            studio.GetName(),
            studio.GetLogo(),
            studio.GetDescription())
        self._cur.execute(request)
        self._db.commit()

    def AddAuthor(self, author: Author):
        request = "INSERT INTO author (first_name, middle_name, last_name, photo, biography)" \
                  "VALUES ('{}', '{}', '{}', '{}', '{}')".format(
            author.GetFirstName(),
            author.GetMiddleName(),
            author.GetLastName(),
            author.GetPhoto(),
            author.GetBiography())
        self._cur.execute(request)
        self._db.commit()

    def AddReview(self, review: Review):
        request = "INSERT INTO review (text, date, rating, nickname, anime_id)" \
                  "VALUES ('{}', '{}', '{}', '{}', '{}')".format(
            review.GetText(),
            review.GetDate(),
            review.GetRating(),
            review.GetNickname(),
            review.GetAnimeId()
        )
        self._cur.execute(request)
        self._db.commit()

    def AddNewGenre(self, name: str):
        request = f"INSERT INTO genre (name) VALUES ('{name}')"
        self._cur.execute(request)
        self._db.commit()

    def AddAnimegenre(self, anime_id: int, genre_id: int):
        request = f"INSERT INTO animegenre (anime_id, genre_id) VALUES ('{anime_id}', '{genre_id}')"
        self._cur.execute(request)
        self._db.commit()

    def AddViewedanime(self, user_id: int, anime_id: int):
        request = f"INSERT INTO viewedanime (user_id, anime_id) VALUES ('{user_id}', '{anime_id}')"
        self._cur.execute(request)
        self._db.commit()

    def ChangeValueInUser(self, var: str, value, user_id: int):
        request = f"UPDATE user SET '{var}' = '{value}' WHERE user_id = '{user_id}'"
        self._cur.execute(request)
        self._db.commit()

    def ChangeValueInAnime(self, var: str, value, anime_id: int):
        request = f"UPDATE anime SET '{var}' = '{value}' WHERE anime_id = '{anime_id}'"
        self._cur.execute(request)
        self._db.commit()

    def ChangeValueInStudio(self, var: str, value, studio_id: int):
        request = f"UPDATE studio SET '{var}' = '{value}' WHERE studio_id = '{studio_id}'"
        self._cur.execute(request)
        self._db.commit()

    def ChangeValueInAuthor(self, var: str, value, author_id: int):
        request = f"UPDATE author SET '{var}' = '{value}' WHERE author_id = '{author_id}'"
        self._cur.execute(request)
        self._db.commit()

    def DeleteRowFromTable(self, table: str, id: int):
        request = f"DELETE FROM '{table}' WHERE id = '{id}'"
        self._cur.execute(request)
        self._db.commit()

    def GetAllAnime(self) -> list:
        ls = []
        self._cur.execute("SELECT * FROM anime")
        for row in self._cur.fetchall():
            anime = Anime(id=row[0], title=row[1], year=str(row[2]), author_id=row[3], studio_id=row[4],
                          format=row[5], description=row[6], poster=row[7])
            ls.append(anime)
        return ls

    def GetAllReviewesOnAnime(self, anime_id: int) -> list:
        ls = []
        self._cur.execute(f"SELECT * FROM review WHERE anime_id = '{anime_id}'")
        for row in self._cur.fetchall():
            review = Review(id=row[0], text=row[1], date=str(row[2]), rating=row[3], nickname=row[4], anime_id=row[5])
            ls.append(review)
        return ls

    def GetUserByLogin(self, login: str) -> User:
        self._cur.execute(f"SELECT * FROM person WHERE login = '{login}'")
        row = self._cur.fetchone()
        user = User(id=row[0], nickname=row[1], login=row[2], password=row[3],
                    avatar=row[4], about_yourself=row[5], registration_date=str(row[6]))
        return user

    def GetAnimeByTitle(self, title: str) -> Anime:
        self._cur.execute(f"SELECT * FROM anime WHERE title = '{title}'")
        row = self._cur.fetchone()
        anime = Anime(id=row[0], title=row[1], year=str(row[2]), author_id=row[3],
                      studio_id=row[4], format=row[5], description=row[6])
        return anime

    def GetAuthorById(self, author_id: str) -> Author:
        self._cur.execute(f"SELECT * FROM author WHERE id = {author_id}")
        row = self._cur.fetchone()
        author = Author(id=row[0], first_name=row[1], middle_name=row[2],
                        last_name=row[3], biography=row[5])
        return author

    def GetStudioById(self, studio_id: str) -> Studio:
        self._cur.execute(f"SELECT * FROM studio WHERE id = {studio_id}")
        row = self._cur.fetchone()
        studio = Studio(id=row[0], name=row[1], description=row[2])
        return studio