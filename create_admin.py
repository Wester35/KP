import os
import sys
from getpass import getpass
from dotenv import load_dotenv

from libs.database import SessionLocal
from controllers.crud import create_user_with_group

def get_app_dir():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))

def load_env():
    env_path = os.path.join(get_app_dir(), ".env")
    load_dotenv(env_path)

def create_admin():
    print("Создание первого администратора:")
    login = input("Логин: ")
    password = getpass("Пароль: ")
    last_name = input("Фамилия: ")
    first_name = input("Имя: ")
    middle_name = input("Отчество (можно Enter): ")
    phone = input("Телефон: ")

    db = SessionLocal()
    try:
        create_user_with_group(
            last_name=last_name,
            first_name=first_name,
            middle_name=middle_name,
            phone=phone,
            login=login,
            password=password,
            group_name=None,
            is_teacher=True,
            is_admin=True
        )
        print("✅ Администратор создан успешно.")
    except Exception as e:
        print("❌ Ошибка при создании администратора:", e)

if __name__ == "__main__":
    load_env()
    create_admin()
