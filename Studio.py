class Studio:
    _id = None
    _name = ""
    _logo = ""
    _description = ""

    def __init__(self, id: int = 0, name: str = "-", logo: str = "-", description: str = "-"):
        self._id = id
        self._name = name
        self._logo = logo
        self._description = description

    def GetId(self) -> int:
        return self._id

    def GetName(self) -> str:
        return self._name

    def GetLogo(self) -> str:
        return self._logo

    def GetDescription(self) -> str:
        return self._description