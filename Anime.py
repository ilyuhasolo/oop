class Anime:
    _id = None
    _title = ""
    _year = ""
    _authorId = None
    _studioId = None
    _format = ""
    _description = ""
    _poster = ""

    def __init__(self, id: int = 0, title: str = "-", year: str = "-", author_id: int = 0, studio_id: int = 0,
                 format: str = "-", description: str = "-", poster: str = "-"):
        self._id = id
        self._title = title
        self._year = year
        self._authorId = author_id
        self._studioId = studio_id
        self._format = format
        self._description = description
        self._poster = poster

    def GetId(self) -> int:
        return self._id

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
