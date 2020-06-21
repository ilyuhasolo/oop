class Anime:
    _title = ""
    _year = ""
    _authorId = None
    _studioId = None
    _format = ""
    _description = ""
    _poster = ""

    def __init__(self, title: str = "", year: str = "", author_id: int = None, studio_id: int = None,
                 format: str = "", description: str = "", poster: str = ""):
        self._title = title
        self._year = year
        self._authorId = author_id
        self._studioId = studio_id
        self._format = format
        self._description = description
        self._poster = poster

    def GetTitle(self) -> str:
        return self._title

    def GetYear(self) -> str:
        return self._year

    def GetAuthorId(self) -> int:
        return self._authorId

    def GetStudioId(self) -> int:
        return self._studioId

    def GetFormat(self) -> str:
        return self._format

    def GetDescription(self) -> str:
        return self._description

    def GetPoster(self) -> str:
        return self._poster
