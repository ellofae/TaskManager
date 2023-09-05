from datetime import datetime

from database.database import session
from models.user import IdentificationForm, User, UserEntity


class UserRepository:
    # Command module
    def save(self, entity: UserEntity) -> User:
        with session() as db:
            'False -> detect only local-column based properties'
            if db.is_modified(entity, include_collections=False):
                entity = db.merge(entity)

            db.add(entity)
            db.commit()
            return User.from_entity(entity)

    def update(self, user: User, user_to_update: UserEntity) -> User:
        if user.email:
            assert user_to_update.email != user.email, 'You cannot change your email to the one you already have'

        assert user_to_update.phone != user.phone, 'You cannot change your phone to the one you already have'

        for key, value in user.dict(exclude_unset=True).items():
            setattr(user_to_update, key, value)

        user_to_update.updated_at = datetime.now()
        return self.save(user_to_update)

    def delete(self, entity: UserEntity) -> User:
        with session() as db:
            db.delete(entity)
            db.commit()

            return User.from_entity(entity)

    # Querying module
    def get_users(self) -> list[User]:
        with session() as db:
            entities = db.query(UserEntity).order_by(UserEntity.id.desc()).all()
            return [User.from_entity(entity) for entity in entities]

    def get_user(self, user_id: int) -> User:
        with session() as db:
            entity = db.query(UserEntity).get(user_id)
            assert entity, f'No user with id {user_id} exists'

            return User.from_entity(entity)

    def get_user_entity(self, user_id: int) -> UserEntity:
        with session() as db:
            entity = db.query(UserEntity).get(user_id)
            assert entity, f'No user with id {user_id} exists'

            return entity

    def check_user_fields(self, user: User) -> None:
        with session() as db:
            if user.email:
                database_entity = db.query(UserEntity).filter(UserEntity.email == user.email).first()
                assert not database_entity, 'Email is already registered'

            if user.phone:
                database_entity = db.query(UserEntity).filter(UserEntity.phone == user.phone).first()
                assert not database_entity, 'Phone number is already registered'

    def get_user_by_credentials(self, user: IdentificationForm) -> UserEntity:
        with session() as db:
            if user.email:
                entity = db.query(UserEntity).filter(UserEntity.email == user.email).first()
                assert entity, 'No user with such email exists'
            elif user.phone:
                entity = db.query(UserEntity).filter(UserEntity.phone == user.phone).first()
                assert entity, 'No user with such phone exists'

            return entity