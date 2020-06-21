class User:
    _nickname = ""
    _login = ""
    _password = None
    _avatar = ""
    _aboutYourself = ""
    _registrationDate = ""

    def __init__(self, nickname: str = "", login: str = "", password: int = None,
                 avatar: str = "", about_yourself: str = "", registration_date: str = ""):
        self._nickname = nickname
        self._login = login
        self._password = password
        self._avatar = avatar
        self._aboutYourself = about_yourself
        self._registrationDate = registration_date

    def GetNickname(self) -> str:
        return self._nickname

    def GetLogin(self) -> str:
        return self._login

    def GetPassword(self) -> int:
        return self._password

    def GetAvatar(self) -> str:
        return self._avatar

    def GetAboutYourself(self) -> str:
        return self._aboutYourself

    def GetRegistrationDate(self) -> str:
        return self._registrationDate
