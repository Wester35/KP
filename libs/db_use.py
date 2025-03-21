from libs.database import SessionLocal, engine
from controllers.crud import create_user_with_group
from libs.database import Base

# from sqlalchemy.orm import configure_mappers
#
# configure_mappers()

db = SessionLocal()



# Base.metadata.drop_all(engine)
# Base.metadata.create_all(engine)

create_user_with_group(
    session=db,
    last_name="Ц",
    first_name="У",
    middle_name="Ю",
    phone="8232938",
    login="ul",
    password="Admin123",
    group_name="ИСП-105",
    is_teacher=False,
    is_admin=False
)