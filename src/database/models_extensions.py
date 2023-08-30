from pydantic import BaseModel

from .database import DatabaseBase


class Base(DatabaseBase):
    'Extended class for declared_base object'
    __abstract__ = True

    def to_dict(self):
        'where .c is a column of a table'
        return {field.name: getattr(self, field.name) for field in self.__table__.c}
    
    @classmethod
    def from_model(cls, model):
        return model.to_entity(cls)

class BaseModelExtended(BaseModel):
    __abstract__ = True
    
    'Extended class for DTO models'
    # def to_entity(self, entity):
    #      return entity(**{field.name: getattr(self, field.name) for field in entity.__table__.c})
    def to_entity(self, entity):
        attributes = {}
        for field in entity.__table__.c:
            if hasattr(self, field.name):
                attributes[field.name] = getattr(self, field.name)
        return entity(**attributes)
    
    @classmethod
    def from_entity(cls, entity):
        return cls(**entity.to_dict())