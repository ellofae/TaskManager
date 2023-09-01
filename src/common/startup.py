from datetime import datetime

import services.hashing as hashing_service
from database.database import session
from decouple import config
from models.user import UserEntity
from models.regular_status import RegularStatus


def startup():
    print('INFO: loading data')

    with session() as db:
        user_record = db.query(UserEntity).filter(UserEntity.status == RegularStatus.ADMIN).first()
        if not user_record:
            password_hashed = hashing_service.password_hashing(config('ADMIN_PASSWORD'))
            admin_user = UserEntity(phone='admin', password=password_hashed, status=RegularStatus.ADMIN, created_at=datetime.now())

            db.add(admin_user)
            db.commit()