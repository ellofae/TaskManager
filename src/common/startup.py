from datetime import datetime

import utils.hashing as hashing_service
from database.database import session
from decouple import config
from models.regular_status import RegularStatus
from models.user import UserEntity


def startup():
    print('START UP INFO: loading data')

    with session() as db:
        user_record = db.query(UserEntity).filter(UserEntity.status == RegularStatus.ADMIN).first()
        if not user_record:
            password_hashed = hashing_service.password_hashing(config('ADMIN_PASSWORD'))
            admin_user = UserEntity(phone='admin', password=password_hashed, status=RegularStatus.ADMIN, created_at=datetime.now())

            db.add(admin_user)
            db.commit()