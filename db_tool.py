import os
import sys

def get_app_dir():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.abspath(__file__))

def create_env_file():
    password = input("Введите пароль от PostgreSQL пользователя 'postgres': ")
    dbname = input("Введите название вашей базы данных: ")

    env_path = os.path.join(get_app_dir(), ".env")
    with open(env_path, "w", encoding="utf-8") as f:
        f.write(f'database_connect="postgresql://postgres:{password}@localhost/{dbname}"\n')

    print(f".env файл успешно создан по пути: {env_path}")



if __name__ == "__main__":
    create_env_file()
