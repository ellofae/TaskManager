from datetime import date
from typing import Optional

from database.models_extensions import Base, BaseModelExtended
from sqlalchemy import Column, Integer, String, DateTime


class CompanyEntity(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    office_location = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)

class Company(BaseModelExtended):
    id: Optional[int] = None
    title: str
    description: Optional[str]
    office_location: Optional[str]

    @classmethod
    def from_entity(cls, entity):
        return cls(**{key: value.strftime("%Y-%m-%d %H:%M:%S") if isinstance(value, date) else value for key, value in
                      entity.to_dict().items()})

    class Config:
        orm_mode = True