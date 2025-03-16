from libs.database import SessionLocal
from libs.crud import create_user_with_group
# from sqlalchemy.orm import configure_mappers
#
# configure_mappers()

db = SessionLocal()

create_user_with_group(
    session=db,
    last_name="Иванов",
    first_name="Иван",
    middle_name="Иванович",
    phone="89101153337",
    login="wester",
    password="Admin123",
    group_name="ИСП-306",
    is_teacher=True,
    is_admin=True
)

# Base.metadata.drop_all(engine)
# Base.metadata.create_all(engine)

