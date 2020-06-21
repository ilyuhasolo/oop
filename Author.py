class Author:
    _firstName = ""
    _middleName = ""
    _lastName = ""
    _photo = ""
    _biography = ""

    def __init__(self, first_name: str = "", middle_name: str = "", last_name: str = "",
                 photo: str = "", biography: str = ""):
        self._firstName = first_name
        self._middleName = middle_name
        self._lastName = last_name
        self._photo = photo
        self._biography = biography

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
