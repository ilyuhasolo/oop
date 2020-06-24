import psycopg2
import User
import Anime
import Author
import Studio
import Review

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
                  "VALUES (?, ?, ?, ?, ?, ?)"
        self._cur.execute(request, [user.GetNickname(), user.GetLogin(), user.GetPassword(),
                                    user.GetAvatar(), user.GetAboutYourself(), user.GetRegistrationDate()])
        self._db.commit()

    def AddAnime(self, anime: Anime):
        request = "INSERT INTO anime (title, year, author_id, studio_id, format, description, poster)" \
                  "VALUES (?, ?, ?, ?, ?, ?, ?)"
        self._cur.execute(request, [anime.GetTitle(), anime.GetYear(), anime.GetAuthorId(), anime.GetStudioId(),
                                    anime.GetFormat(), anime.GetDescription(), anime.GetPoster()])
        self._db.commit()


    def AddStudio(self, studio: Studio):
        request = "INSERT INTO studio (name, logo, description)" \
                  "VALUES (?, ?, ?)"
        self._cur.execute(request, [studio.GetName(), studio.GetLogo(), studio.GetDescription()])
        self._db.commit()

    def AddAuthor(self, author: Author):
        request = "INSERT INTO author (first_name, middle_name, last_name, photo, biography)" \
                  "VALUES (?, ?, ?, ?, ?)"
        self._cur.execute(request, [author.GetFirstName(), author.GetMiddleName(), author.GetLastName(),
                                    author.GetPhoto(), author.GetBiography()])
        self._db.commit()

    def AddNewGenre(self, name: str):
        request = f"INSERT INTO genre (name) VALUES (?)"
        self._cur.execute(request, name)
        self._db.commit()

    def AddAnimegenre(self, anime_id: int, genre_id: int):
        request = f"INSERT INTO animegenre (anime_id, genre_id) VALUES (?, ?)"
        self._cur.execute(request, [anime_id, genre_id])
        self._db.commit()

    def AddViewedanime(self, user_id: int, anime_id: int):
        request = f"INSERT INTO viewedanime (user_id, anime_id) VALUES ({user_id}, {anime_id})"
        self._cur.execute(request)
        self._db.commit()

    def ChangeValueInUser(self, var: str, value, user_id: int):
        request = "UPDATE user SET ? = ? WHERE user_id = ?"
        self._cur.execute(request, [var, value, user_id])
        self._db.commit()

    def ChangeValueInAnime(self, var: str, value, anime_id: int):
        request = "UPDATE anime SET ? = ? WHERE anime_id = ?"
        self._cur.execute(request, [var, value, anime_id])
        self._db.commit()

    def ChangeValueInStudio(self, var: str, value, studio_id: int):
        request = "UPDATE studio SET ? = ? WHERE studio_id = ?"
        self._cur.execute(request, [var, value, studio_id])
        self._db.commit()

    def ChangeValueInAuthor(self, var: str, value, author_id: int):
        request = "UPDATE author SET ? = ? WHERE author_id = ?"
        self._cur.execute(request, [var, value, author_id])
        self._db.commit()

    def DeleteRowFromTable(self, table: str, id: int):
        request = "DELETE FROM ? WHERE id = ?"
        self._cur.execute(request, [table, id])
        self._db.commit()

    def GetAllAnime(self) -> list:
        ls = []
        self._cur.execute("SELECT * FROM anime")
        for row in self._cur.fetchall():
            anime = Anime(title=row[1], year=row[2], author_id=row[3], studio_id=row[4],
                          format=row[5], description=row[6], poster=row[7])
            ls.append(anime)
        return ls

    def GetAllReviewesOnAnime(self, anime_id: int) -> list:
        ls = []
        self._cur.execute("SELECT * FROM review WHERE user_id = ?", anime_id)
        for row in self._cur.fetchall():
            review = Review(text=row[1], date=row[2], rating=row[3], user_id=row[4])
            ls.append(review)
        return ls

    def GetUserByLogin(self, login: str) -> User:
        self._cur.execute("SELECT * FROM person WHERE login = ?", login)
        row = self._cur.fetchone()
        user = User(nickname=row[1], login=row[2], password=row[3],
                    avatar=row[4], about_yourself=row[5], registration_date=row[6])
        return user
