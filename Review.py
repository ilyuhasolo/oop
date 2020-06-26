class Review:
    _id = None
    _text = ""
    _date = ""
    _rating = None
    _nickname = ""
    _animeId = None

    def __init__(self, id: int = 0, text: str = "-", date: str = "-", rating: int = 0,
                 nickname: str = "-", anime_id: int = 0):
        self._id = id
        self._text = text
        self._date = date
        self._rating = rating
        self._nickname = nickname
        self._animeId = anime_id

    def GetId(self) -> int:
        return self._id

    def GetText(self) -> str:
        return self._text

    def GetDate(self) -> str:
        return self._date

    def GetRating(self) -> int:
        return self._rating

    def GetNickname(self) -> str:
        return self._nickname

    def GetAnimeId(self) -> int:
        return  self._animeId