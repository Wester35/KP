import json
from sqlalchemy.orm import Session
from libs.database import SessionLocal
from models.User import User
from models.Group import Group
from models.Journal import Journal
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date


def save_user_session(user_id):
    with open("libs/user_session.json", "w") as f:
        json.dump({"user_id": user_id}, f)


def load_user_session():
    try:
        with open("libs/user_session.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None


def check_if_logged_in():
    session_data = load_user_session()
    if session_data:
        user_id = session_data.get("user_id")
        db = SessionLocal()
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            return user
    return None


def create_user(session: Session, last_name, first_name, middle_name, phone, login, password, group_id, is_teacher=False, is_admin=False):
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


def get_students_with_journal(group_id):
    """Получает всех студентов группы и их опоздания, если они есть."""
    db: Session = SessionLocal()

    results = (
        db.query(
            User.last_name,
            User.first_name,
            User.middle_name,
            Journal.status
        )
        .outerjoin(Journal, User.id == Journal.user_id)  # LEFT JOIN
        .filter(User.group_id == group_id, User.is_teacher == False, User.is_admin == False)
        .order_by(User.last_name, User.first_name)
        .all()
    )

    db.close()
    return results
