import json
import os
from sqlalchemy import func, and_
from sqlalchemy.orm import Session
from libs.database import SessionLocal
from models.User import User
from models.Group import Group
from models.Journal import Journal
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date, datetime


def save_user_session(user_id):
    with open("libs/user_session.json", "w") as f:
        json.dump({"user_id": user_id}, f)


def delete_user_session():
    auth_file_path = "libs/user_session.json"
    if os.path.exists(auth_file_path):
        os.remove(auth_file_path)


def load_user_session():
    try:
        with open("libs/user_session.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None


def get_user_data_by_id(user_id):
    db: Session = SessionLocal()
    user = (
        db.query(User.id,
                 User.first_name,
                 User.last_name,
                 User.middle_name,
                 User.phone,
                 User.login,
                 User.photo,
                 User.group_id,
                 Group.name.label("group_name"))
        .outerjoin(Group)
        .filter(User.id == user_id)
        .first()
    )
    db.close()
    return user


def check_if_logged_in():
    session_data = load_user_session()
    if session_data:
        user_id = session_data.get("user_id")
        db = SessionLocal()
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            return user.id, user.is_teacher, user.is_admin
    return None, None, None


def create_user(session: Session, last_name, first_name, middle_name, phone, login,
                password, group_id, is_teacher=False, is_admin=False):
    hashed_password = generate_password_hash(password)
    new_user = User(
        last_name=last_name,
        first_name=first_name,
        middle_name=middle_name,
        phone=phone,
        login=login,
        password=hashed_password,
        group_id=group_id,
        is_teacher=is_teacher,
        is_admin=is_admin
    )
    session.add(new_user)
    session.commit()
    return new_user


def authenticate_user(session: Session, login, password):
    user = session.query(User).filter_by(login=login).first()
    if user and check_password_hash(user.password, password):
        return user
    return None


def add_attendance(session: Session, user_id, lesson_number, status):
    entry = Journal(user_id=user_id, date=date.today(), lesson_number=lesson_number, status=status)
    session.add(entry)
    session.commit()
    return entry


def get_attendance_by_user(session: Session, user_id):
    return session.query(Journal).filter_by(user_id=user_id).all()


def create_user_with_group(session: Session, last_name, first_name, middle_name, phone, login, password, group_name,
                           is_teacher=False, is_admin=False):

    group = session.query(Group).filter_by(name=group_name).first()

    if not group:
        group = Group(name=group_name)
        session.add(group)
        session.commit()

    hashed_password = generate_password_hash(password)

    new_user = User(
        last_name=last_name,
        first_name=first_name,
        middle_name=middle_name,
        phone=phone,
        login=login,
        password=hashed_password,
        group_id=group.id,
        is_teacher=is_teacher,
        is_admin=is_admin
    )

    session.add(new_user)
    session.commit()


def get_groups_from_db():
    db = SessionLocal()
    groups = db.query(Group).all()
    db.close()
    return groups


def get_students_with_journal(group_id, date_str):
    """Получает всех студентов группы и их опоздания за указанную дату и все 7 пар."""
    db: Session = SessionLocal()

    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Ошибка: неверный формат даты, ожидается YYYY-MM-DD")
        return []

    results = (
        db.query(
            User.last_name,
            User.first_name,
            User.middle_name,
            func.coalesce(Journal.status, "").label("status"),
            Journal.lesson_number
        )
        .outerjoin(Journal, and_(User.id == Journal.user_id, Journal.date == date_obj))
        .filter(
            User.group_id == group_id,
            User.is_teacher == False,
            User.is_admin == False
        )
        .order_by(User.last_name, User.first_name, Journal.lesson_number)
        .all()
    )

    db.close()
    student_dict = {}
    for last_name, first_name, middle_name, status, lesson_number in results:
        key = (last_name, first_name, middle_name)
        if key not in student_dict:
            student_dict[key] = [""] * 7
        if lesson_number is not None:
            student_dict[key][lesson_number - 1] = status

    return student_dict


def update_or_create_journal_entry(db: Session, last_name: str, first_name: str, middle_name: str, lesson_number: int,
                                   status: str, date_str):
    """Обновляет запись о посещаемости или создаёт новую, если её нет."""
    student = db.query(User).filter(
        User.last_name == last_name,
        User.first_name == first_name,
        User.middle_name == (middle_name if middle_name else None)
    ).first()

    if not student:
        return False

    try:
        today = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Ошибка: неверный формат даты, ожидается YYYY-MM-DD")
        return []

    entry = db.query(Journal).filter(
        Journal.user_id == student.id,
        Journal.date == today,
        Journal.lesson_number == lesson_number
    ).first()

    if entry:
        entry.status = status
    else:
        new_entry = Journal(
            user_id=student.id,
            date=today,
            lesson_number=lesson_number,
            status=status
        )
        db.add(new_entry)

    db.commit()
    return True
