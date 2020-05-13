import psycopg2

connection = psycopg2.connect(
    database="oop",
    user="postgres",
    password="1234567890",
    host="localhost",
    port="5432"
)


def add_new_user(nickname, login, password, avatar, about_yourself, registration_date):
    """Добавляет нового пользователя в базу данных"""
    cursor = connection.cursor()
    request = ("INSERT INTO person (nickname, login, password, avatar, about_yourself, registration_date)" +
               f"VALUES ('{nickname}', '{login}', {password}, '{avatar}', '{about_yourself}', '{registration_date}')")
    cursor.execute(request)
    connection.commit()


def add_new_genre(name):
    """Добавляет новый жанр в базу данных"""
    cursor = connection.cursor()
    request = f"INSERT INTO genre (name) VALUES ('{name}')"
    cursor.execute(request)
    connection.commit()


def add_animegenre(anime_id, genre_id):
    """Присваевает аниме новый жанр"""
    cursor = connection.cursor()
    request = f"INSERT INTO animegenre (anime_id, genre_id) VALUES ({anime_id}, {genre_id})"
    cursor.execute(request)
    connection.commit()


def add_new_anime(title, year, author_id, studio_id, format, description, poster):
    """Добавляет новое аниме в базу данных"""
    cursor = connection.cursor()
    request = ("INSERT INTO anime (title, year, author_id, studio_id, format, description, poster)" +
               f"VALUES ('{title}', '{year}', {author_id}, {studio_id}, '{format}', '{description}', '{poster}')")
    cursor.execute(request)
    connection.commit()


def add_new_studio(name, logo, description):
    """Добавляет новую студию в базу данных"""
    cursor = connection.cursor()
    request = f"INSERT INTO studio (name, logo, description) VALUES ('{name}', '{logo}', '{description}')"
    cursor.execute(request)
    connection.commit()


def add_new_author(first_name, middle_name, last_name, photo, biography):
    """Добавляет нового автора в базу данных"""
    cursor = connection.cursor()
    request = ("INSERT INTO author (first_name, middle_name, last_name, photo, biography)" +
               f"VALUES ('{first_name}', '{middle_name}', '{last_name}', '{photo}', '{biography}'")
    cursor.execute(request)
    connection.commit()


def add_viewedanime(user_id, anime_id):
    """Добавляет запись о просмотре anime_id пользователем user_id"""
    cursor = connection.cursor()
    request = f"INSERT INTO viewedanime (user_id, anime_id) VALUES ({user_id}, {anime_id})"
    cursor.execute(request)
    connection.commit()


def change_information_about_user(user_id, about_yourself):
    """Обновляет значение поля 'О себе' пользователя user_id"""
    cursor = connection.cursor()
    request = f"UPDATE person SET about_yourself = '{about_yourself}' WHERE id = {user_id}"
    cursor.execute(request)
    connection.commit()


def change_user_nickname(user_id, new_nickname):
    """Изменяет никнейм пользователя user_id"""
    cursor = connection.cursor()
    request = f"UPDATE person SET nickname = '{new_nickname}' WHERE id = {user_id}"
    cursor.execute(request)
    connection.commit()


def change_user_avatar(user_id, new_avatar):
    """Изменяет аватар пользователя user_id на new_avatar"""
    cursor = connection.cursor()
    request = f"UPDATE person SET avatar = '{new_avatar}' WHERE id = {user_id}'"
    cursor.execute(request)
    connection.commit()


def change_anime_description(anime_id, new_description):
    """Изменяет описание аниме"""
    cursor = connection.cursor()
    request = f"UPDATE anime SET description = '{new_description}' WHERE anime_id = {anime_id}"
    cursor.execute(request)
    connection.commit()


def change_anime_poster(anime_id, new_poster):
    """Изменяет постер аниме"""
    cursor = connection.cursor()
    request = f"UPDATE anime SET poster = '{new_poster}' WHERE anime_id = {anime_id}"
    cursor.execute(request)
    connection.commit()


def change_studio_logo(studio_id, new_logo):
    """Изменяет лого студии"""
    cursor = connection.cursor()
    request = f"UPDATE studio SET logo = '{new_logo}' WHERE studio_id = {studio_id}"
    cursor.execute(request)
    connection.commit()


def change_studio_description(studio_id, new_description):
    """Изменяет описание студии"""
    cursor = connection.cursor()
    request = f"UPDATE studio SET description = '{new_description}' WHERE studio_id = {studio_id}"
    cursor.execute(request)
    connection.commit()


def change_author_photo(author_id, new_photo):
    """Изменяет фотографию автора"""
    cursor = connection.cursor()
    request = f"UPDATE author SET photo = '{new_photo}' WHERE author_id = {author_id}"
    cursor.execute(request)
    connection.commit()


def change_author_biography(author_id, new_biography):
    """Изменяет биографию автора"""
    cursor = connection.cursor()
    request = f"UPDATE author SET biography = '{new_biography}' WHERE author_id = {author_id}"
    cursor.execute(request)
    connection.commit()


def delete_user(user_id):
    """Удаляет запись о пользователе user_id из базы данных"""
    cursor = connection.cursor()
    request = f"DELETE FROM person WHERE id = {user_id}"
    cursor.execute(request)
    connection.commit()


def delete_author(author_id):
    """Удаляет запись об author_id из базы данных"""
    cursor = connection.cursor()
    request = f"DELETE FROM author WHERE id = {author_id}"
    cursor.execute(request)
    connection.commit()


def delete_studio(studio_id):
    """Удаляет запись о studio_id из базы данных"""
    cursor = connection.cursor()
    request = f"DELETE FROM studio WHERE id = {studio_id}"
    cursor.execute(request)
    connection.commit()


def delete_anime(anime_id):
    """Удаляет запись об anime_id из базы данных"""
    cursor = connection.cursor()
    request = f"DELETE FROM anime WHERE id = {anime_id}"
    cursor.execute(request)
    connection.commit()


def delete_genre(genre_id):
    """Удаляет запись о genre_id из базы данных"""
    cursor = connection.cursor()
    request = f"DELETE FROM genre WHERE id = {genre_id}"
    cursor.execute(request)
    connection.commit()


def delete_viewedanime(anime_id, user_id):
    """Удаляет запись о просмотре user_id anime_id"""
    cursor = connection.cursor()
    request = f"DELETE FROM viewedanime WHERE user_id = {user_id} AND anime_id = {anime_id}"
    cursor.execute(request)
    connection.commit()


def delete_review(anime_id, user_id):
    """Удаляет отзыв об anime_id пользователя user_id"""
    cursor = connection.cursor()
    request = f"DELETE FROM review WHERE user_id = {user_id} AND anime_id = {anime_id}"
    cursor.execute(request)
    connection.commit()


def get_review_by_user(user_id):
    """Возвращает все отзывы написанные пользователем user_id"""
    cursor = connection.cursor()
    request = f"SELECT text, date, rating, anime_id FROM review WHERE user_id = {user_id}"
    cursor.execute(request)
    return cursor.fetchall()


def get_review_by_anime(anime_id):
    """Возвращает все отзывы написанные на anime_id"""
    cursor = connection.cursor()
    request = f"SELECT text, date, rating, user_id FROM review WHERE anime_id = {anime_id}"
    cursor.execute(request)
    return cursor.fetchall()


def get_anime_by_genre(genre_id):
    """Получает все аниме в жанре genre_id"""
    cursor = connection.cursor()
    request = ("SELECT anime_id, title, year, author_id, studio_id, format, description, poster" +
               "FROM anime INNER JOIN animegenre ON anime.id = animegenre.anime_id" +
               f"WHERE genre_id = {genre_id}")
    cursor.execute(request)
    return cursor.fetchall()


def get_genre_by_anime(anime_id):
    """Получает все жанры anime_id"""
    cursor = connection.cursor()
    request = ("SELECT genre_id, name" +
               "FROM genre INNER JOIN animegenre ON animegenre.genre_id = genre.id" +
               f"WHERE anime_id = {anime_id}")
    cursor.execute(request)
    return cursor.fetchall()


def get_anime_viewed_by_user(user_id):
    """Получает всё анимэ, просмотренное пользователем user_id"""
    cursor = connection.cursor()
    request = ("SELECT anime_id, title, year, author_id, studio_id, format, description, poster" +
               "FROM anime INNER JOIN viewedanime ON anime.id = viewedanime.anime_id" +
               f"WHERE user_id = {user_id}")
    cursor.execute(request)
    return cursor.fetchall()


def get_anime_viewed_count(anime_id):
    """Получает у скольких пользователей anime_id отмечено как просмотренное"""
    cursor = connection.cursor()
    request = f"SELECT count(*) FROM viewedanime WHERE anime_id = {anime_id}"
    cursor.execute(request)
    return cursor.fetchone()[0]


def get_anime_by_studio(studio_id):
    """Получает всё анимэ, созданное студией studio_id"""
    cursor = connection.cursor()
    request = f"SELECT * FROM anime WHERE studio_id = {studio_id}"
    cursor.execute(request)
    return cursor.fetchall()


def get_anime_by_author(author_id):
    """Получает всё аниме, созданное автором author_id"""
    cursor = connection.cursor()
    request = f"SELECT * FROM anime WHERE author_id = {author_id}"
    cursor.execute(request)
    return cursor.fetchall()
