class Review:
    _text = ""
    _date = ""
    _rating = None
    _userId = None
    _animeId = None

    def __init__(self, text: str = "-", date: str = "-", rating: int = 0,
                 user_id: int = 0, anime_id: int = 0):
        self._text = text
        self._date = date
        self._rating = rating
        self._userId = user_id
        self._animeId = anime_id

    def GetText(self) -> str:
        return self._text

    def GetDate(self) -> str:
        return self._date

    def GetRating(self) -> int:
        return self._rating

    def GetUserId(self) -> int:
        return self._userId

    def GetAnimeId(self) -> int:
        return  self._animeId