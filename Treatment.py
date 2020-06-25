import socket
import threading
import json
from dbase import DataBase
from Anime import Anime
from User import User
from Review import Review


class Treatment(threading.Thread):
    _sock = None
    _id = None
    _dbase = None
    _callback = None

    def __init__(self, socket: socket.socket, id, callback):
        threading.Thread.__init__(self)
        self._sock = socket
        self._id = id
        self._callback = callback
        self._dbase = DataBase("test1", "1234567890")

    def start(self) -> None:
        while True:
            try:
                input_data = self._GetDataFromSocket()
            except Exception:
                break
            command = self._GetCommand(input_data)
            arguments = self._GetArguments(input_data, command)
            output_data = self._ExecuteCommand(command, arguments)
            try:
                self._SendDataToSocket(output_data)
            except Exception:
                break
        self._callback("Worker " + str(self._id) + ": Closed")

    def _GetDataFromSocket(self) -> str:
        raw_data = self._sock.recv(1024)
        if not raw_data:
            raise Exception()
        return str(raw_data, "ascii")

    def _GetCommand(self, data: str) -> str:
        input = json.loads(data)
        result = list(input.keys())[0]
        return result

    def _GetArguments(self, data: str, command: str) -> dict:
        input = json.loads(data)
        result = input[command]
        return result

    def _ExecuteCommand(self, command: str, arguments: dict):
        result = ""
        if command == "AddUser":
            self.AddUser(arguments)
        elif command == "AddAnime":
            self.AddAnime(arguments)
        elif command == "AddReview":
            self.AddReview(arguments)
        elif command == "GetAnimeByTitle":
            result = self.GetAnimeByTitle(arguments)
        elif command == "GetUserByLogin":
            result = self.GetUserByLogin(arguments)

        return result

    def _SendDataToSocket(self, data):
        if data is not None:
            data_in_bytes = bytes(data, 'ascii')
            total_send_bytes = len(data_in_bytes)
            current_send_bytes = 0
            while current_send_bytes != total_send_bytes:
                current_send_bytes += self._sock.send(data_in_bytes)

    def AddUser(self, arguments):
        self._callback("Worker " + str(self._id) + ": User adding...")
        user = User(
            nickname=arguments["nickname"],
            login=arguments["login"],
            password=arguments["password"],
            about_yourself=arguments["about_yourself"],
            registration_date=arguments["registration_date"]
        )
        self._dbase.AddUser(user)
        self._callback("Worker " + str(self._id) + ": Done")

    def AddAnime(self, arguments):
        self._callback("Worker " + str(self._id) + ": Anime adding...")
        anime = Anime(
            title=arguments["title"],
            year=arguments["year"],
            author_id=arguments["author_id"],
            studio_id=arguments["studio_id"],
            format=arguments["format"],
            description=arguments["description"]
        )
        self._dbase.AddAnime(anime)
        self._callback("Done")

    def AddReview(self, arguments):
        self._callback("Worker " + str(self._id) + ": Review adding...")
        review = Review(
            text=arguments["text"],
            date=arguments["date"],
            rating=arguments["rating"],
            user_id=arguments["user_id"],
            anime_id=arguments["anime_id"]
        )
        self._dbase.AddReview(review)
        self._callback("Worker " + str(self._id) + ": Done")

    def GetAnimeByTitle(self, arguments):
        self._callback("Worker " + str(self._id) + ": Anime searching...")
        res = {}
        try:
            anime = self._dbase.GetAnimeByTitle(arguments["title"])
            res = {
                "title": anime.GetTitle(),
                "year": anime.GetYear(),
                "author_id": anime.GetAuthorId(),
                "studio_id": anime.GetStudioId(),
                "format": anime.GetFormat(),
                "description": anime.GetDescription()
            }
            self._callback("Worker " + str(self._id) + ": Done")
        except Exception:
            self._callback("Worker " + str(self._id) + ": Error")
        return json.dumps(res)

    def GetUserByLogin(self, arguments):
        self._callback("Worker " + str(self._id) + ": User searching...")
        res = {}
        try:
            user = self._dbase.GetUserByLogin(arguments["login"])
            res = {
                "login": user.GetLogin(),
                "nickname": user.GetNickname(),
                "password": user.GetPassword(),
                "avatar": user.GetAvatar(),
                "registration_date": user.GetRegistrationDate(),
                "about_yourself": user.GetAboutYourself()
            }
            self._callback("Worker " + str(self._id) + ": Done")
        except Exception:
            self._callback("Worker " + str(self._id) + ": Error")
        return json.dumps(res)
