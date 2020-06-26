class User:
    _id = None
    _nickname = ""
    _login = ""
    _password = None
    _avatar = ""
    _aboutYourself = ""
    _registrationDate = ""

    def __init__(self, id: int = 0, nickname: str = "-", login: str = "-", password: str = "-",
                 avatar: str = "-", about_yourself: str = "-", registration_date: str = "-"):
        self._id = id
        self._nickname = nickname
        self._login = login
        self._password = password
        self._avatar = avatar
        self._aboutYourself = about_yourself
        self._registrationDate = registration_date

    def GetId(self) -> int:
        return self._id

    def GetNickname(self) -> str:
        return self._nickname

    def GetLogin(self) -> str:
        return self._login

    def GetPassword(self) -> str:
        return self._password

    def GetAvatar(self) -> str:
        return self._avatar

    def GetAboutYourself(self) -> str:
        return self._aboutYourself

    def GetRegistrationDate(self) -> str:
        return self._registrationDate
