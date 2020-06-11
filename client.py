from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
"""import datab.py as datab"""
import datetime
import hashlib


login = ""
password = ""

class Coder():
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
                now = datetime.datetime.now()
                string = Coder.code(password1)
                print(string)
                """datab.add_new_user(nickname, Coder.code(password1), avatar, about_yourself, str(now.date))"""
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
        main_window = MainWindow()
        main_window.geometry('600x600')
        main_window.resizable(width=False, height=False)
        main_window.mainloop()


class MainWindow(Tk):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        listbox = Listbox(width=50, height=9)
        listbox.place(relx=0.25, rely=0.1)
        listbox.insert(0, "naruto")
        select = listbox.curselection()
        listbox.bind("<<ListboxSelect>>", lambda event, arg=listbox: self.open_anime(event, arg))
        add_button = Button(self, text="Добавить", command=lambda:[self.add_anime(listbox)])
        add_button.place(relx=0, rely=0)
        self.MainWindowUpdate()

    def add_anime(self, listbox):
    	add_window= AddWindow(listbox)
    	add_window.mainloop()

    def open_anime(self, event, arg):
    	title = Label(text=arg.get(ACTIVE))
    	title.place(relx=0.6, rely=0.5)
    	

    def MainWindowUpdate(self):
    	pass

class AddWindow(Tk):
    def __init__(self, listbox, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        name_text = Label(self, text="Название аниме: ").pack()
        name_entry = Entry(self)
        name_entry.pack()
        description_text = Label(self, text="Описание : ").pack()
        description_entry = Text(self, height=10, width=20)
        description_entry.pack()
        author_text = Label(self, text="Автор : ").pack()
        author_entry = Entry(self)
        author_entry.pack()
        ok_button=Button(self, text="OK", command=lambda:[self.okClick(listbox, name_entry.get(),description_entry.get(1.0, tk.END),author_entry.get())])
        ok_button.pack()
        cancel_button=Button(self, text="CANCEL", command=self.destroy)
        cancel_button.pack()

    def okClick(self, listbox, name, description, author):
        listbox.insert(END, name)
        self.destroy()


if __name__ == '__main__':
    reg_window = RegWindow()
    reg_window.geometry('300x500')
    reg_window.mainloop()
