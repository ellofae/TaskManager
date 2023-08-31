from datetime import datetime

import services.hashing as hashing_service
from database.database import session
from decouple import config
from models.user import UserEntity


def startup():
    print('loading data')

    with session() as db:
        user_record = db.query(UserEntity).filter(UserEntity.status == 'admin').first()
        if not user_record:
            password_hashed = hashing_service.password_hashing(config('ADMIN_PASSWORD'))
            admin_user = UserEntity(phone='admin', password=password_hashed, status='admin', created_at=datetime.now())

            db.add(admin_user)
            db.commit()