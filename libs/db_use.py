from libs.database import SessionLocal, engine
from controllers.crud import create_user_with_group, create_user
from libs.database import Base

# from sqlalchemy.orm import configure_mappers
#
# configure_mappers()

db = SessionLocal()



# Base.metadata.drop_all(engine)
# Base.metadata.create_all(engine)
#
# create_user(
#     session=db,
#     last_name="A",
#     first_name="B",
#     middle_name="C",
#     phone="7",
#     login="west",
#     password="Admin123",
#     group_id=None,
#     is_teacher=True,
#     is_admin=True
# )


import random

students_data = [
    ("ИСП-105", 4),
    ("ИСП-110", 5),
    ("ИСП-206", 6),
    ("ИСП-306", 5),
    ("ИСП-407", 8),
    ("ИБ-210", 2),
    ("Р-312", 7),
    ("СИС-301", 3),
]

first_names = ["Алексей", "Иван", "Петр", "Максим", "Егор", "Дмитрий", "Артем", "Владимир", "Сергей", "Никита"]
last_names = ["Смирнов", "Иванов", "Кузнецов", "Соколов", "Попов", "Лебедев", "Козлов", "Новиков", "Морозов", "Петров"]
middle_names = ["Алексеевич", "Иванович", "Петрович", "Максимович", "Егорович", "Дмитриевич", "Артемович", "Владимирович", "Сергеевич", "Никитович"]

db = SessionLocal()
student_id = 1

for group_name, count in students_data:
    for _ in range(count):
        last_name = random.choice(last_names)
        first_name = random.choice(first_names)
        middle_name = random.choice(middle_names)
        phone = str(random.randint(8000000000, 8999999999))
        login = f"ul{student_id}"

        create_user_with_group(
            session=db,
            last_name=last_name,
            first_name=first_name,
            middle_name=middle_name,
            phone=phone,
            login=login,
            password="Admin123",
            group_name=group_name,
            is_teacher=False,
            is_admin=False
        )

        student_id += 1

db.commit()
db.close()
