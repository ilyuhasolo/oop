from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import socket
import tkinter as tk
from PIL import Image, ImageTk
import datetime
import hashlib
import json

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
sock.connect(('localhost', 7777))


class Serv():
	def add_user(self, nickname, login, password, about_yourself, now):
		res = {
			"AddUser": {
				"nickname" : nickname,
				"login": login,
				"password": password,
				"about_yourself" : about_yourself,
				"registration_date" : str(now)
				}
		}
		sock.sendall(bytes(json.dumps(res), "ascii"))

	def add_anime(self, title, year, author, studio, genre, description, poster):
		res = {
			"AddAnime":{
				"title" : title,
				"year" : year,
				"author_id" : author,
				"studio_id" : studio,
				"format" : genre,
				"description" : description
			}
		}
		sock.sendall(bytes(json.dumps(res), "ascii"))

	def add_review(self, review, rating, user_id, anime_id, date):
		res = {
			"AddReview":{
				"text": review,
				"date": date,
				"rating" : rating,
				"user_id" : user_id,
				"anime_id" : anime_id
			}
		}
		sock.sendall(bytes(json.dumps(res),'ascii'))

	def get_user_by_login(self, login):
		res = {
			"GetUserByLogin" : {
				"login" : login
			}
		}
		sock.sendall(bytes(json.dumps(res), 'ascii'))
		user = str(sock.recv(1024), 'ascii')
		return json.loads(user)

	#def get_all_anime(self):
        #pass

	def get_anime_by_title(self):
		pass

	def get_all_reviews_on_anime(self):
		pass

class Coder(): #превращает пароль в хэш
    def code(password):
    	coded = hashlib.md5(password.encode())
    	return coded.hexdigest()

class RegWindow(Tk):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)

        text = Label(text="Для входа в систему зарегистрируйтесь !")
        text_login = Label(text="Введите логин* : ")
        registr_login = Entry()
        text_password1 = Label(text="Введи пароль* : ")
        registr_password1 = Entry(show="*")
        text_password2 = Label(text="Повтори пароль* : ")
        registr_password2 = Entry(show="*")
        text_nickname = Label(text="Введи никнейм* : ")
        registr_nickname = Entry()
        avatar = Label(text="Аватар", borderwidth=2, relief="ridge")
        avatar_button = Button(self, text = "Выбрать аватар", command = lambda:[self.openfile(avatar)])
        about_yourself = Label(text = "Расскажи о себе")
        about_yourself_entry = Text(self, height = 10, width = 40)
        avatar.photo = None
        button_registr = Button(self, text="Зарегистрироваться", command=lambda:[self.reg_button_clicked(registr_login.get(),registr_password1.get(),registr_password2.get(), registr_nickname.get(), avatar.photo,about_yourself_entry.get(1.0, tk.END))])
        button_alreadyhas = Button(self, text="Уже есть аккаунт", command=lambda:[self.alreadyhas_button_clicked()])
        text.pack()
        text_login.pack()
        registr_login.pack()
        text_password1.pack()
        registr_password1.pack()
        text_password2.pack()
        registr_password2.pack()
        text_nickname.pack()
        registr_nickname.pack()
        avatar.pack(pady=5)
        avatar_button.pack(pady=5)
        about_yourself.pack()
        about_yourself_entry.pack()
        button_registr.pack()
        button_alreadyhas.pack()

    def openfile(self, avatar):
        filename = filedialog.askopenfilename()
        image = Image.open(filename)
        resize = image.resize((60,65), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(resize)
        avatar.config(image = photo, height = 60, width = 65)
        avatar.photo = photo

    def reg_button_clicked(self, login, password1, password2, nickname, avatar, about_yourself):
        if password1 == password2:
            if login and password1 and password2 and nickname != "":
                self.destroy()
                now = datetime.datetime.now() #здесь добавить проверку по логину
                serv = Serv()
                serv.add_user(nickname=nickname, login=login, password=Coder.code(password1), about_yourself=about_yourself, now=now)
                log_window = LogWindow()
                log_window.geometry('300x500')
                log_window.mainloop()
            else: messagebox.showerror("Ошибка!", "Заполните обязательные поля под звездочкой!")
        else: messagebox.showerror("Ошибка!", "Пароли не совпадают")

    def alreadyhas_button_clicked(self):
        self.destroy()
        log_window = LogWindow()
        log_window.geometry('300x500')
        log_window.mainloop()


class LogWindow(Tk):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)

        text_enter_login = Label(self, text="Введите логин : ")
        enter_login = Entry(self)
        text_enter_pass = Label(self, text="Введите пароль : ")
        enter_password = Entry(self, show="*")
        button_login = Button(self, text="Войти", command = lambda:[self.log_button_clicked(enter_login.get(), enter_password.get())])
        text_enter_login.pack()
        enter_login.pack()
        text_enter_pass.pack()
        enter_password.pack()
        button_login.pack()

    def log_button_clicked(self, login, password):
        self.destroy()
        if self.check_login(login, password):
            main_window = MainWindow() #Здесь надо будет посылать id
            main_window.geometry('600x600')
            main_window.resizable(width=False, height=False)
            main_window.mainloop()
        else: messagebox.showerror("Ошибка", "Неправильный логин/пароль")

    def check_login(self, login, password): #проверка пароля соответствующего логину по хэшу
        coded = Coder.code(password)
        s = Serv()
        user = s.get_user_by_login(login)
        if coded == user["password"]:
            return True
        else: return False


class AdminWindow(Tk):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        listbox = Listbox(width=50, height=9)
        listbox.place(relx=0.25, rely=0.1)
        title = Label()
        title.place(relx=0.4, rely=0.35)
        poster = Label()
        poster.place(relx=0.1, rely=0.4)
        year = Label()
        year.place(relx=0.35, rely=0.4)
        author = Label()
        author.place(relx=0.35, rely=0.44)
        genres = Label()
        genres.place(relx=0.35, rely=0.48)
        studio = Label()
        studio.place(relx=0.35, rely=0.52)
        desc = Label()
        desc.place(relx=0, rely=0.6)
        container = Frame(self, height=5, width=600)
        canvas = Canvas(container)
        container.place(relx=0, rely=0.7, relheight=0.3, relwidth=1)
        canvas.place(relx=0,rely=0, relheight=1, relwidth=1)
        scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)
        listbox.bind("<<ListboxSelect>>", lambda event, arg=listbox: self.open_anime(event, arg, title, poster, year, author, genres, studio, desc, container, canvas,scrollbar))
        add_button = Button(self, text="Добавить", command=lambda:[self.add_anime(listbox)])
        add_button.place(relx=0, rely=0)
        self.MainWindowUpdate(listbox)

    def add_anime(self, listbox):
    	add_window= AddWindow(listbox, self)
    	add_window.mainloop()

    def open_anime(self, event, arg, title, poster, year, author, genres, studio, desc, container, canvas, scrollbar):
    	canvas.delete("all")
    	scrollbar.pack_forget()
    	scrollbar.pack(side="right", fill="y")
    	title.config(text=arg.get(ACTIVE))
    	poster.config(text = "poster", height=5, width=10, borderwidth=2, relief="ridge")
    	year.config(text="year")
    	author.config(text="author")
    	genres.config(text="genres")
    	studio.config(text="studio")
    	desc.config(text="description")
    	scrollable_frame = Frame(canvas)
    	scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    	canvas.create_window((0,0), window=scrollable_frame, anchor="nw")
    	canvas.configure(yscrollcommand=scrollbar.set)
        
    	for i in range(50):
    		ScrolableReview(scrollable_frame).pack(pady=10)
    	

    def MainWindowUpdate(self, listbox): #вызывается после добавления, изменения или удаления. Берет данные из базы
        listbox.delete(0, tk.END)
        all_anime = Serv.get_all_anime()
        for i in range(all_anime):
            listbox.insert(all_anime[i])
        pass

class AddWindow(Tk):
    def __init__(self, listbox, parent, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        title_text = Label(self, text="Название аниме: ").pack()
        title_entry = Entry(self)
        title_entry.pack()
        year_text = Label(self, text="Год выхода: ").pack()
        year_entry = Entry(self)
        year_entry.pack()
        author_text = Label(self, text="Автор : ").pack()
        author_entry = Entry(self)
        author_entry.pack()
        studio_text = Label(self, text="Студия: ").pack()
        studio_entry = Entry(self)
        studio_entry.pack()
        format_text = Label(self, text="Жанр: ").pack()
        format_entry = Entry(self)
        format_entry.pack()
        description_text = Label(self, text="Описание : ").pack()
        description_entry = Text(self, height=10, width=20)
        description_entry.pack()
        poster = Label(self, width=10, height = 5, text = "Постер", borderwidth=2, relief="ridge")
        poster.photo = None
        poster.pack()
        poster.bind("<Button-1>", lambda e, arg=poster: self.change_poster(e, poster))
        ok_button=Button(self, text="OK", command=lambda:[self.okClick(parent, listbox, title_entry.get(), year_entry.get(), author_entry.get(), studio_entry.get(), format_entry.get(), description_entry.get(1.0, tk.END), poster.photo)])
        ok_button.pack()
        cancel_button=Button(self, text="CANCEL", command=self.destroy)
        cancel_button.pack()

    def okClick(self, parent, listbox, title, year, author, studio, genre, description, poster):
        s = Serv("localhost", 8889)
        s.add_anime(title, year, author, studio, genre, description, poster)
        parent.MainWindowUpdate(listbox)
        self.destroy()

    def change_poster(self, event, poster):
        filename = filedialog.askopenfilename()
        image = Image.open(filename)
        resize = image.resize((60,65), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(resize, master=poster)
        poster.config(image = photo, height = 60, width = 65)
        poster.photo = photo

class MainWindow(Tk):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        avatar = Label(height=5, width=10, text="avatar", borderwidth=2, relief="ridge")
        #здесь загрузка аватара
        avatar.place(relx=0.01, rely=0.01)
        nickname = Label(text="nickname")
        nickname.place(relx=0.02, rely=0.15)
        listbox = Listbox(width=50, height=9)
        listbox.place(relx=0.25, rely=0.1)
        listbox.insert(0, "naruto")
        listbox.insert(1, "boruto")
        select = listbox.curselection()
        title = Label()
        title.place(relx=0.4, rely=0.4)
        poster = Label()
        poster.place(relx=0.1, rely=0.5)
        year = Label()
        year.place(relx=0.35, rely=0.5)
        author = Label()
        author.place(relx=0.35, rely=0.54)
        genres = Label()
        genres.place(relx=0.35, rely=0.58)
        studio = Label()
        studio.place(relx=0.35, rely=0.62)
        desc = Label()
        desc.place(relx=0, rely=0.7)
        container = Frame(height=5, width=600)
        canvas = Canvas(container)
        scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)
        container.place(relx=0, rely=0.8, relheight=0.2, relwidth=1)
        canvas.place(relx=0,rely=0, relheight=1, relwidth=1)
        add_review_button = Button(self, text="Добавить", width=10, command=lambda:[self.add_review(canvas, scrollbar)])
        listbox.bind("<<ListboxSelect>>", lambda event, arg=listbox: self.open_anime(event, arg, title, poster, year, author, genres, studio, desc, add_review_button, canvas, scrollbar))

    def open_anime(self, event, arg, title, poster, year, author, genres, studio, desc, add_review_button, canvas, scrollbar):
    	scrollbar.pack_forget()
    	add_review_button.place_forget()
    	add_review_button.place(relx=0.8, rely=0.75)
    	scrollbar.pack(side="right", fill="y")
    	self.MainWindowUpdate(canvas, scrollbar)
    	title.config(text=arg.get(ACTIVE))
    	poster.config(text = "poster", height=5, width=10, borderwidth=2, relief="ridge")
    	year.config(text="year")
    	author.config(text="author")
    	genres.config(text="genres")
    	studio.config(text="studio")
    	desc.config(text="description")
    	
    def add_review(self, canvas, scrollbar):
    	add=AddReview(self, canvas, scrollbar)
    	add.mainloop()

    def MainWindowUpdate(self, canvas, scrollbar): #вызывается после добавления, изменения или удаления. Берет данные из базы
    	canvas.delete("all")
    	scrollable_frame = Frame(canvas)
    	scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    	canvas.create_window((0,0), window=scrollable_frame, anchor="nw")
    	canvas.configure(yscrollcommand=scrollbar.set)
    	for i in range(10):
    		a = ScrolableReview(scrollable_frame)
    		a.construct("nickname","avatar", "review","rating","date")

class ScrolableReview(Label):
	def __init__(self, *arg, **kwarg):
		super().__init__(*arg, **kwarg)
		self.pack(pady=5, fill="x")

	def construct(self, nickname, avatar, review, rating, date):
		Label(self, text=avatar, borderwidth=2, relief="ridge", height=5, width=10).pack(side="left")
		Label(self, text=nickname).place(relx=0.01, rely=0)
		Label(self, text=review).place(rely=0, relx=0.3)
		Label(self, text=rating).pack(side="right", padx=400)
		Label(self, text=date).pack(side="left", padx=5)

class AddReview(Tk):
	def __init__(self, parent, canvas, scrollbar, *arg, **kwarg):
		super().__init__(*arg, **kwarg)
		Label(self,text="Оставьте отзыв").pack()
		review = Text(self, height=10 ,width=20)
		review.pack()
		Label(self,text="Оценка: ").pack()
		rating = ttk.Combobox(self, values=["1","2","3","4","5","6","7","8","9","10"])
		rating.pack()
		ok_button = Button(self, text="OK", width=10, command=lambda:[self.OKClick(parent, review.get(1.0, tk.END), rating.get(), "user_id", "anime_id", canvas, scrollbar)])
		ok_button.pack()
		close_button = Button(self, text="Отмена", width=10, command=self.destroy)
		close_button.pack()

	def OKClick(self, parent, review, rating, user_id, anime_id, canvas, scrollbar):
		s = Serv()
		d = datetime.datetime.now()
		s.add_review(review, rating, user_id, anime_id, d)
		parent.MainWindowUpdate(canvas, scrollbar)
		self.destroy()

if __name__ == '__main__':
    reg_window = RegWindow()
    reg_window.geometry('300x500')
    reg_window.mainloop()