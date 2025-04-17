import json
import os
from sqlalchemy import func, and_, case
from sqlalchemy.orm import Session
from libs.database import SessionLocal
from models.LessonLog import LessonLog
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


def save_image_path_to_db(user_id, image_path):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.photo = image_path
        db.commit()
    db.close()


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


def create_user_with_group(session: Session, last_name, first_name, middle_name, phone,
                           login, password, group_name, is_teacher=False, is_admin=False):
    group = None
    if group_name is not None:
        group = session.query(Group).filter_by(name=group_name).first()
        if not group:
            group = Group(name=group_name)
            session.add(group)
            session.commit()

    group_id = group.id if group else None

    return create_user(
        session=session,
        last_name=last_name,
        first_name=first_name,
        middle_name=middle_name,
        phone=phone,
        login=login,
        password=password,
        group_id=group_id,
        is_teacher=is_teacher,
        is_admin=is_admin
    )


def get_groups_from_db():
    db = SessionLocal()
    groups = db.query(Group).all()
    db.close()
    return groups


def get_students_with_journal(group_id, date_str):
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


def update_or_create_journal_entry(last_name: str,
                                   first_name: str, middle_name: str, lesson_number: int,
                                   status: str, date_str: str, teacher_id):
    db = SessionLocal()
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
            status=status,
            teacher_id=teacher_id
        )
        db.add(new_entry)

    db.commit()
    db.close()
    return True


def update_or_create_log_entry(teacher_id, group_id, lesson_number: int,
                                date_str: str, lesson_data: str):
    db = SessionLocal()

    try:
        today = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Ошибка: неверный формат даты, ожидается YYYY-MM-DD")
        db.close()
        return False

    try:
        entry = db.query(LessonLog).filter_by(
            teacher_id=teacher_id,
            group_id=group_id,
            lesson_number=lesson_number,
            date=today
        ).first()

        if entry:
            entry.lesson_data = lesson_data
        else:
            entry = LessonLog(
                teacher_id=teacher_id,
                group_id=group_id,
                lesson_number=lesson_number,
                date=today,
                lesson_data=lesson_data
            )
            db.add(entry)

        db.commit()
        return True

    except Exception as e:
        print(f"Ошибка при сохранении записи: {e}")
        db.rollback()
        return False

    finally:
        db.close()



def get_statuses_from_logs(group_id, date_str):
    db: Session = SessionLocal()

    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Ошибка: неверный формат даты, ожидается YYYY-MM-DD")
        return []

    results = (
        db.query(
            LessonLog.lesson_number,
            LessonLog.lesson_data
        )
        .filter(
            LessonLog.group_id == group_id,
            LessonLog.date == date_obj
        )
        .order_by(LessonLog.lesson_number)
        .all()
    )

    db.close()

    lessons = [""] * 7
    for lesson_number, lesson_data in results:
        if 1 <= lesson_number <= 7:
            lessons[lesson_number - 1] = lesson_data or ""

    return lessons


def count_statuses_by_student(user_id):
    db: Session = SessionLocal()

    results = (
        db.query(
            func.sum(case((Journal.status == "н", 1), else_=0)).label("count_n"),
            func.sum(case((Journal.status == "о", 1), else_=0)).label("count_o")
        )
        .filter(Journal.user_id == user_id)
        .one()
    )

    db.close()

    count_n, count_o = results

    return {
        "н": count_n,
        "о": count_o
    }


def get_lates_and_absences_by_date(user_id):
    db: Session = SessionLocal()

    results = (
        db.query(
            Journal.date,
            func.count(case((Journal.status == "н", 1))).label("absences"),
            func.count(case((Journal.status == "о", 1))).label("lates")
        )
        .filter(Journal.user_id == user_id)
        .group_by(Journal.date)
        .order_by(Journal.date)
        .all()
    )

    db.close()

    return results


def count_lessons_for_group(group_id: int):
    db: Session = SessionLocal()

    count = (
        db.query(func.count())
        .filter(
            LessonLog.group_id == group_id,
            LessonLog.lesson_data != "",
            LessonLog.lesson_data.isnot(None)
        )
        .scalar()
    )

    db.close()
    return count
