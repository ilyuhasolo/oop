from tkinter import *
from tkinter import messagebox


login = ""
password = ""

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
        button_login = Button(self, text="Войти")
        text_enter_login.pack()
        enter_login.pack()
        text_enter_pass.pack()
        enter_password.pack()
        button_login.pack()

    def log_button_clicked(self):


if __name__ == '__main__':
    reg_window = RegWindow()
    reg_window.geometry('300x500')
    reg_window.mainloop()
