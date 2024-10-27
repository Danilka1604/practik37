import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

root = tk.Tk()
root.title("San-tech - Авторизация")
root.geometry("400x500")
root.configure(bg="white")

try:
    image = Image.open("yandexart-fbvut9o6qs51ivn6k3ng.jpeg")
    image = image.resize((150, 150), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image)
except Exception as e:
    print("Ошибка при загрузке изображения:", e)
    img = None


def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "user" and password == "password":
        messagebox.showinfo("Успех", "Вы успешно вошли в систему!")
    else:
        messagebox.showerror("Ошибка", "Неправильный логин или пароль")

def register():
    messagebox.showinfo("Регистрация", "Переход на страницу регистрации.")

def forgot_password():
    messagebox.showinfo("Восстановление пароля", "Переход на страницу восстановления пароля.")

if img:
    logo_label = tk.Label(root, image=img, bg="white")
    logo_label.pack(pady=20)

title_label = tk.Label(root, text="Вход в San-tech", font=("Arial", 20), bg="white", fg="black")
title_label.pack(pady=10)

frame_username = tk.Frame(root, bg="white")
frame_username.pack(pady=10)
username_label = tk.Label(frame_username, text="Логин:", font=("Arial", 12), bg="white")
username_label.pack(side=tk.LEFT)
entry_username = tk.Entry(frame_username, width=25, font=("Arial", 12))
entry_username.pack(side=tk.LEFT)

frame_password = tk.Frame(root, bg="white")
frame_password.pack(pady=10)
password_label = tk.Label(frame_password, text="Пароль:", font=("Arial", 12), bg="white")
password_label.pack(side=tk.LEFT)
entry_password = tk.Entry(frame_password, width=25, font=("Arial", 12), show="*")
entry_password.pack(side=tk.LEFT)

login_button = tk.Button(root, text="Войти", command=login, font=("Arial", 12), width=20, bg="#4CAF50", fg="white")
login_button.pack(pady=20)

register_button = tk.Button(root, text="Зарегистрироваться", command=register, font=("Arial", 10), fg="blue", bd=0, bg="white")
register_button.pack(pady=5)

forgot_button = tk.Button(root, text="Забыли пароль?", command=forgot_password, font=("Arial", 10), fg="blue", bd=0, bg="white")
forgot_button.pack(pady=5)

root.mainloop()
