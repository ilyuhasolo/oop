class Author:
    _id = None
    _firstName = ""
    _middleName = ""
    _lastName = ""
    _photo = ""
    _biography = ""

    def __init__(self, id: int = 0, first_name: str = "-", middle_name: str = "-", last_name: str = "-",
                 photo: str = "-", biography: str = "-"):
        self._id = id
        self._firstName = first_name
        self._middleName = middle_name
        self._lastName = last_name
        self._photo = photo
        self._biography = biography

    def GetId(self) -> int:
        return self._id

    def GetFirstName(self) -> str:
        return self._firstName

    def GetMiddleName(self) -> str:
        return self._middleName

    def GetLastName(self) -> str:
        return self._lastName

    def GetPhoto(self) -> str:
        return self._photo

    def GetBiography(self) -> str:
        return self._biography
