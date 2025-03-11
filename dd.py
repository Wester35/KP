from libs.database import SessionLocal
from libs.crud import create_user, get_user_by_username, verify_password
from libs.models import RoleEnum

# Подключение к БД
db = SessionLocal()

# Создаем пользователей
create_user(db, "admin", "admin", RoleEnum.ADMIN, "Администратор")
create_user(db, "teacher", "teacher4", RoleEnum.TEACHER, "Учитель Иванов")
create_user(db, "student", "student1", RoleEnum.STUDENT, "Студент Петров")


# Проверяем авторизацию
user = get_user_by_username(db, "student1")
if user and verify_password(user, "studentpassword"):
    print(f"Успешный вход: {user.username} с ролью {user.role}")
else:
    print("Ошибка аутентификации!")

# Закрываем сессию
db.close()

# from libs.database import engine, Base
# import libs.models  # Импортируем модели, чтобы SQLAlchemy их увидел
#
# print("Создаю таблицы в базе данных...")
# Base.metadata.create_all(bind=engine)
# print("Таблицы успешно созданы!")