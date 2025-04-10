from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()


class Providers(Base):
    __tablename__ = "Providers"
    provider_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(45), nullable=False)
    lastname = Column(String(45), nullable=False)
    phone = Column(String(45), nullable=False)
