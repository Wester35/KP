from sqlalchemy.orm import Session
from .models import User, Student, Attendance, RoleEnum
from werkzeug.security import generate_password_hash, check_password_hash

# Добавить студента
def create_student(db: Session, name: str, group: str):
    student = Student(name=name, group=group)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student


# Отметить присутствие / опоздание
def mark_attendance(db: Session, student_id: int, date, pair_number: int, is_late: bool):
    record = Attendance(student_id=student_id, date=date, pair_number=pair_number, is_late=is_late)
    db.add(record)
    db.commit()
    db.refresh(record)
    return record


# Получить посещаемость за дату и номер пары
def get_attendance_by_date_and_pair(db: Session, date, pair_number: int):
    return db.query(Attendance).filter(Attendance.date == date, Attendance.pair_number == pair_number).all()
# Создание пользователя


def create_user(db: Session, username: str, password: str, role: RoleEnum):
    hashed_password = generate_password_hash(password)  # Хэшируем пароль
    user = User(username=username, password=hashed_password, role=role)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# Получение пользователя по логину
def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

# Проверка пароля
def verify_password(user: User, password: str):
    return check_password_hash(user.password, password)