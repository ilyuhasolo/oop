from tkinter import *
from tkinter import messagebox
import tkinter as tk


login = ""
password = ""
 
class Anime(tk.Frame):
    def __init__(self, anime_name, desc, author, *args, **kwargs):
           tk.Frame.__init__(self)

           self.name= Label(self, text=anime_name)
           self.name.pack(side="left")
           self.description = Label(self, text=desc)
           self.description.pack(side="left", padx=10)
           self.author = Label(self, text=author)
           self.author.pack(side="left", padx=10)
           self.edit = Button(self, text="Редактировать", command=self.regButton)
           self.edit.pack(side="left", padx=10)
           self.edit = Button(self, text="Удалить", command=self.destroy)
           self.edit.pack(side="left", padx=10)

    def regButton(self):
    	ed_window = EditWindow(self)
    	ed_window.mainloop()
        


class RegWindow(Tk):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)

        text = Label(text="Для входа в систему зарегистрируйтесь !")
        text_login = Label(text="Введите логин : ")
        registr_login = Entry()
        text_password1 = Label(text="Введите пароль : ")
        registr_password1 = Entry(show="*")
        text_password2 = Label(text="Повторите пароль : ")
        registr_password2 = Entry(show="*")
        button_registr = Button(self, text="Зарегистрироваться", command=lambda:[self.reg_button_clicked(registr_login.get(),registr_password1.get(),registr_password2.get())])
        button_alreadyhas = Button(self, text="Уже есть аккаунт", command=lambda:[self.alreadyhas_button_clicked()])
        text.pack()
        text_login.pack()
        registr_login.pack()
        text_password1.pack()
        registr_password1.pack()
        text_password2.pack()
        registr_password2.pack()
        button_registr.pack()
        button_alreadyhas.pack()

    def reg_button_clicked(self, registr_login, registr_password1, registr_password2):
        if registr_password1 == registr_password2:
            self.destroy()
            global login
            login = registr_login
            global password
            password = registr_password1
            log_window = LogWindow()
            log_window.geometry('300x500')
            log_window.mainloop()
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
        button_login = Button(self, text="Войти", command = self.log_button_clicked)
        text_enter_login.pack()
        enter_login.pack()
        text_enter_pass.pack()
        enter_password.pack()
        button_login.pack()

    def log_button_clicked(self):
    	self.destroy()
    	adm_window = AdminWindow()
    	adm_window.geometry('600x600')
    	adm_window.resizable(width=False, height=False)
    	adm_window.mainloop()


class AdminWindow(Tk):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        add_button = Button(self, text="Добавить", command=self.add_anime)
        add_button.place(x=20, y=20)

    def add_anime(self):
    	   add_window= AddWindow()
    	   add_window.mainloop()

class AddWindow(Tk):
    def __init__(self, *arg, **kwarg):
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
        ok_button=Button(self, text="OK", command=lambda:[self.okClick(name_entry.get(),description_entry.get(1.0, tk.END),author_entry.get())])
        ok_button.pack()
        cancel_button=Button(self, text="CANCEL", command=self.destroy)
        cancel_button.pack()

    def okClick(self, name, description, author):
        Anime(name, description, author).pack()
        self.destroy()

class EditWindow(Tk):
    def __init__(self, parent, *arg, **kwarg):
        super().__init__(*arg, **kwarg)

        name_text = Label(self, text="Название аниме: ").pack()
        name_entry = Text(self, height=1, width=15)
        name_entry.pack()
        name_entry.insert(1.0, parent.name.cget("text"))
        description_text = Label(self, text="Описание : ").pack()
        description_entry = Text(self, height=10, width=15)
        description_entry.pack()
        description_entry.insert(1.0, parent.description.cget("text"))
        author_text = Label(self, text="Автор : ").pack()
        author_entry = Text(self, height=1, width=15)
        author_entry.pack()
        author_entry.insert(1.0, parent.author.cget("text"))
        ok_button=Button(self, text="OK", command=lambda:[self.okClick(parent, name_entry.get(1.0, tk.END),description_entry.get(1.0, tk.END),author_entry.get(1.0, tk.END))])
        ok_button.pack()
        cancel_button=Button(self, text="CANCEL", command=self.destroy)
        cancel_button.pack()

    def okClick(self, parent, name, desc, author):
        parent.name["text"] = name
        parent.description["text"] = desc
        parent.author["text"] = author
        self.destroy()

if __name__ == '__main__':
    reg_window = RegWindow()
    reg_window.geometry('300x500')
    reg_window.mainloop()
