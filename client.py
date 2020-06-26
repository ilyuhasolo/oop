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

	def add_anime(self, title, year, author_id, studio_id, genre, description):
		res = {
			"AddAnime":{
				"title" : title,
				"year" : year,
				"author_id" : author_id,
				"studio_id" : studio_id,
				"format" : genre,
				"description" : description
			}
		}
		sock.sendall(bytes(json.dumps(res), "ascii"))

	def add_review(self, review, rating, nickname, anime_id, date):
		res = {
			"AddReview":{
				"text": review,
				"date": str(date),
				"rating" : rating,
				"nickname" : nickname,
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

	def get_all_anime(self):
		res = {
			"GetAllAnime": {}
		}
		sock.sendall(bytes(json.dumps(res), 'ascii'))

		animes = str(sock.recv(4096), 'ascii')
		return json.loads(animes)

	def get_anime_by_title(self, title):
		res = {
			"GetAnimeByTitle" : {
				"title" : title
			}
		}
		sock.sendall(bytes(json.dumps(res), 'ascii'))
		anime = str(sock.recv(1024), 'ascii')
		return json.loads(anime)

	def get_all_reviews_on_anime(self, anime_id):
		res = {
			"GetAllReviewsOnAnime" : {
				"id" : anime_id
			}
		}
		sock.sendall(bytes(json.dumps(res), 'ascii'))
		reviews = str(sock.recv(1024), 'ascii')
		return json.loads(reviews)

	def get_author_by_id(self, author_id):
		res = {
			"GetAuthorById" : {
				"id" : author_id
			}
		}
		sock.sendall(bytes(json.dumps(res), 'ascii'))
		author = str(sock.recv(1024), 'ascii')
		return json.loads(author)

	def get_studio_by_id(self, studio_id):
		res = {
			"GetStudioById" : {
				"id" : studio_id
			}
		}
		sock.sendall(bytes(json.dumps(res), 'ascii'))
		studio = str(sock.recv(1024), 'ascii')
		return json.loads(studio)

	def add_author(self, first_name, middle_name, last_name, biography):
		res = {
			"AddAuthor":{
				"first_name" : first_name,
				"middle_name" : middle_name,
				"last_name" : last_name,
				"biography" : biography
			}
		}
		sock.sendall(bytes(json.dumps(res), 'ascii'))

	def add_studio(self, name, description):
		res = {
			"AddStudio":{
				"name" : name,
				"description" : description
			}
		}
		sock.sendall(bytes(json.dumps(res), 'ascii'))

class Coder(): #превращает пароль в хэш
    def code(password):
    	coded = hashlib.md5(password.encode())
    	return coded.hexdigest()

serv = Serv()

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
        about_yourself = Label(text = "Расскажи о себе")
        about_yourself_entry = Text(self, height = 10, width = 40)
        button_registr = Button(self, text="Зарегистрироваться", command=lambda:[self.reg_button_clicked(registr_login.get(),registr_password1.get(),registr_password2.get(), registr_nickname.get(),about_yourself_entry.get(1.0, tk.END))])
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
        about_yourself.pack()
        about_yourself_entry.pack()
        button_registr.pack()
        button_alreadyhas.pack()

    def reg_button_clicked(self, login, password1, password2, nickname, about_yourself):
        if password1 == password2:
            if login and password1 and password2 and nickname != "":
                self.destroy()
                usr = serv.get_user_by_login(login)
                if not usr:
                    now = datetime.datetime.now()
                   #serv = Serv()
                    serv.add_user(nickname=nickname, login=login, password=Coder.code(password1), about_yourself=about_yourself, now=now)
                    log_window = LogWindow()
                    log_window.geometry('300x500')
                    log_window.mainloop()
                else: messagebox.showerror("Ошибка", "Пользователь с таким логином уже существует")
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
        user = serv.get_user_by_login(login)
        if self.check_login(user, password):
            self.destroy()
            if user["login"] == "admin":
            	admin_window = AdminWindow()
            	admin_window.geometry('600x600')
            	admin_window.resizable(width=False, height=False)
            	admin_window.mainloop()
            else:
            	main_window = MainWindow(user) #Здесь надо будет посылать id
            	main_window.geometry('600x600')
            	main_window.resizable(width=False, height=False)
            	main_window.mainloop()
        else:
            messagebox.showerror("Ошибка", "Неправильный логин/пароль")

    def check_login(self, user, password): #проверка пароля соответствующего логину по хэшу
        coded = Coder.code(password)
        #s = Serv()
        if coded == user["password"]:
            return True
        else: return False


class AdminWindow(Tk):
    _anime = None
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        add_anime_button = Button(self, text="Добавить аниме", width=15, command=lambda:[self.add_anime(listbox)])
        add_anime_button.place(relx = 0.77, rely = 0.06)
        add_author_button = Button(self, text="Добавить автора", width=15, command=lambda:[self.add_author()])
        add_author_button.place(relx = 0.77, rely = 0.12)
        add_studio_button = Button(self, text="Добавить студию", width=15, command=lambda:[self.add_studio()])
        add_studio_button.place(relx = 0.77, rely = 0.18)
        listbox = Listbox(width=50, height=9)
        listbox.pack()
        title = Label()
        title.pack(pady = 10)
        year = Label()
        year.pack(pady= 10)
        author = Label()
        author.pack(pady=5)
        genres = Label()
        genres.pack(pady=5)
        studio = Label()
        studio.pack(pady=5)
        desc = Label(wraplength = 600)
        desc.pack(pady=5)
        rev = Label(self)
        rev.pack()
        container = Frame(self, height=5, width=600)
        canvas = Canvas(container)
        container.pack(pady=10, fill="x")
        canvas.pack(side="left", fill="both", expand = True)
        scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)
        listbox.bind("<<ListboxSelect>>", lambda event, arg=listbox: self.open_anime(event, arg, rev, title, year, author, genres, studio, desc, container, canvas,scrollbar))
        self.AnimeListUpdate(listbox)

    def add_anime(self, listbox):
    	add_window= AddWindow(listbox, self)
    	add_window.mainloop()

    def add_author(self):
    	add_window = AddAuthorWindow()
    	add_window.mainloop()

    def add_studio(self):
    	add_window = AddStudioWindow()
    	add_window.mainloop()

    def open_anime(self, event, arg, rev, title, year, author, genres, studio, desc, container, canvas, scrollbar):
    	canvas.delete("all")
    	rev.configure(text="Отзывы", font=("Times New Roman", 16, "bold"))
    	scrollbar.pack_forget()
    	scrollbar.pack(side="right", fill="y")
    	self._anime = serv.get_anime_by_title(arg.get(ACTIVE))
    	at = serv.get_author_by_id(self._anime["author_id"])
    	st = serv.get_studio_by_id(self._anime["studio_id"])
    	title.config(text=self._anime["title"], font=("TimesNewRoman", 20, "bold"))
    	year.config(text='Год выхода: ' + self._anime["year"])
    	author.config(text='Автор: ' + at["first_name"] + ' ' + at["middle_name"] + ' ' + at["last_name"])
    	genres.config(text='Жанр: ' + self._anime["format"])
    	studio.config(text='Студия: ' + st["name"])
    	desc.config(text='Описание: ' + self._anime["description"])
    	scrollable_frame = Frame(canvas)
    	scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    	canvas.create_window((0,0), window=scrollable_frame, anchor="nw")
    	canvas.configure(yscrollcommand=scrollbar.set)
    	reviews = serv.get_all_reviews_on_anime(self._anime["id"])
    	for i in reviews:
    		rev = ScrolableReview(scrollable_frame)
    		rev.construct(i)
    	

    def AnimeListUpdate(self, listbox): #вызывается после добавления, изменения или удаления. Берет данные из базы
        listbox.delete(0, tk.END)
        all_anime = serv.get_all_anime()
        for i in all_anime:
            listbox.insert(tk.END, i["title"])
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
        ok_button=Button(self, text="OK", command=lambda:[self.okClick(parent, listbox, title_entry.get(), year_entry.get(), author_entry.get(), studio_entry.get(), format_entry.get(), description_entry.get(1.0, tk.END))])
        ok_button.pack()
        cancel_button=Button(self, text="CANCEL", command=self.destroy)
        cancel_button.pack()

    def okClick(self, parent, listbox, title, year, author, studio, genre, description):
        serv.add_anime(title, year, author, studio, genre, description)
        parent.AnimeListUpdate(listbox)
        self.destroy()

class MainWindow(Tk):
    _anime = None
    def __init__(self, user, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        #здесь загрузка аватара
        fr = Frame()
        fr.place(relx=0, rely=0, width=100, height=20)
        nickname = Label(fr, text=user["nickname"], font='Helvetica 12')
        nickname.pack(side="right")
        listbox = Listbox(width=50, height=9)
        listbox.pack()
        self.AnimeListUpdate(listbox)
        select = listbox.curselection()
        title = Label()
        title.pack(pady=10)
        year = Label()
        year.pack(pady=5)
        author = Label()
        author.pack(pady=5)
        genres = Label()
        genres.pack(pady=5)
        studio = Label()
        studio.pack(pady=5)
        desc = Label(wraplength = 600)
        desc.pack(pady=5)
        rev = Label(self)
        rev.pack()
        container = Frame(self, height=5, width=600)
        canvas = Canvas(container)
        container.pack(pady=10, fill="x")
        canvas.pack(side="left", fill="both", expand = True)
        scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)
        add_review_button = Button(self, text="Добавить отзыв", width=15, command=lambda:[self.add_review(canvas, scrollbar, user)])
        listbox.bind("<<ListboxSelect>>", lambda event, arg=listbox: self.open_anime(event, arg, rev, title, year, author, genres, studio, desc, add_review_button, canvas, scrollbar))

    def AnimeListUpdate(self, listbox):
        all_anime = serv.get_all_anime()
        for i in all_anime:
        	listbox.insert(tk.END, i["title"])

    def open_anime(self, event, arg, title, year, author, genres, studio, desc, add_review_button, canvas, scrollbar):
    	self._anime = serv.get_anime_by_title(arg.get(ACTIVE))
    	rev.configure(text="Отзывы", font=("Times New Roman", 16, "bold"))
    	scrollbar.pack_forget()
    	add_review_button.place_forget()
    	add_review_button.place(relx=0.77, rely=0.08)
    	scrollbar.pack(side="right", fill="y")
    	self.ReviewsUpdate(canvas, scrollbar)
    	at = serv.get_author_by_id(self._anime["author_id"])
    	st = serv.get_studio_by_id(self._anime["studio_id"])
    	title.config(text=self._anime["title"], font=("TimesNewRoman", 20, "bold"))
    	year.config(text='Год выхода: ' + self._anime["year"])
    	author.config(text='Автор: ' + at["first_name"] + ' ' + at["middle_name"] + ' ' + at["last_name"])
    	genres.config(text='Жанр: '+ self._anime["format"])
    	studio.config(text='Студия: ' + st["name"])
    	desc.config(text='Описание: ' + self._anime["description"])
    	
    def add_review(self, canvas, scrollbar, user):
    	add=AddReview(self, canvas, scrollbar, user, self._anime)
    	add.mainloop()

    def ReviewsUpdate(self, canvas, scrollbar): #вызывается после добавления, изменения или удаления. Берет данные из базы
    	canvas.delete("all")
    	scrollable_frame = Frame(canvas)
    	scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    	canvas.create_window((0,0), window=scrollable_frame, anchor="nw")
    	canvas.configure(yscrollcommand=scrollbar.set)
    	reviews = serv.get_all_reviews_on_anime(self._anime["id"])
    	for i in reviews:
    		rev = ScrolableReview(scrollable_frame)
    		rev.construct(i)

class ScrolableReview(Label):
	def __init__(self, *arg, **kwarg):
		super().__init__(*arg, **kwarg)
		self.pack(pady=5, fill="x")

	def construct(self, review):
		Label(self, text=review["nickname"]).place(relx=0.2, rely=0)
		Label(self, text=review["text"]).place(rely=0, relx=0.3)
		Label(self, text=review["rating"]).pack(side="right", padx=400)
		Label(self, text=review["date"]).pack(side="left", padx=5)

class AddReview(Tk):
	def __init__(self, parent, canvas, scrollbar, user, anime, *arg, **kwarg):
		super().__init__(*arg, **kwarg)
		Label(self,text="Оставьте отзыв").pack()
		review = Text(self, height=10 ,width=20)
		review.pack()
		Label(self,text="Оценка: ").pack()
		rating = ttk.Combobox(self, values=["1","2","3","4","5","6","7","8","9","10"])
		rating.pack()
		ok_button = Button(self, text="OK", width=10, command=lambda:[self.OKClick(parent, user, anime, review.get(1.0, tk.END), rating.get(), canvas, scrollbar)])
		ok_button.pack()
		close_button = Button(self, text="Отмена", width=10, command=self.destroy)
		close_button.pack()

	def OKClick(self, parent, user, anime, review, rating, canvas, scrollbar):
		#s = Serv()
		d = datetime.datetime.strftime(datetime.datetime.now(), "%Y.%m.%d %H:%M")
		serv.add_review(review, rating, user["nickname"], anime["id"],  d)
		parent.ReviewsUpdate(canvas, scrollbar)
		self.destroy()

class AddAuthorWindow(Tk):
	def __init__(self, *arg, **kwarg):
		super().__init__(*arg, **kwarg)
		Label(self,text="Имя автора:").pack()
		first_name = Entry(self)
		first_name.pack()
		Label(self,text="Отчество автора:").pack()
		middle_name = Entry(self)
		middle_name.pack()
		Label(self,text="Фамилия автора:").pack()
		last_name = Entry(self)
		last_name.pack()
		Label(self, text="Описание автора:").pack()
		desc = Text(self, width=20, height = 10)
		desc.pack()
		ok_button = Button(self, text="OK", width=10, command=lambda:[self.OKClick(first_name.get(), middle_name.get(), last_name.get(), desc.get(1.0, tk.END))])
		ok_button.pack()
		close_button = Button(self, text="Отмена", width=10, command=self.destroy)
		close_button.pack()

	def OKClick(self, first_name, middle_name, last_name, description):
		serv.add_author(first_name, middle_name, last_name, description)
		self.destroy()

class AddStudioWindow(Tk):
	def __init__(self, *arg, **kwarg):
		super().__init__(*arg, **kwarg)
		Label(self,text="Название: ").pack()
		name = Entry(self)
		name.pack()
		Label(self, text="Описание студии:").pack()
		desc = Text(self, width=20, height = 10)
		desc.pack()
		ok_button = Button(self, text="OK", width=10, command=lambda:[self.OKClick(name.get(), desc.get(1.0, tk.END))])
		ok_button.pack()
		close_button = Button(self, text="Отмена", width=10, command=self.destroy)
		close_button.pack()

	def OKClick(self, name,  description):
		serv.add_studio(name, description)
		self.destroy()


if __name__ == '__main__':
    reg_window = RegWindow()
    reg_window.geometry('300x500')
    reg_window.mainloop()