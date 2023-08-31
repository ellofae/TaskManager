from pydantic import Field
from typing import Optional
from database.models_extensions import Base, BaseModelExtended
from sqlalchemy import Column, Integer, String, DateTime


class CompanyEntity(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    office_location = Column(String, nullable=True)

class Company(BaseModelExtended):
    id: Optional[int] = None
    title: str
    description: Optional[str]
    office_location: Optional[str]

    class Config:
        orm_mode = True