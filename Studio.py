class Studio:
    _name = ""
    _logo = ""
    _description = ""

    def __init__(self, name: str = "-", logo: str = "-", description: str = "-"):
        self._name = name
        self._logo = logo
        self._description = description

    def GetName(self) -> str:
        return self._name

    def GetLogo(self) -> str:
        return self._logo

    def GetDescription(self) -> str:
        return self._description