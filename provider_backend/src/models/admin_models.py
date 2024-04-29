from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class AdminInfos(Base):
    __tablename__ = "admin_infos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
    credentials = relationship("AdminCredential", back_populates="admin")

class AdminCredential(Base):
    __tablename__ = "admin_credential"

    id = Column(Integer, primary_key=True, autoincrement=True)
    password = Column(String)
    salt = Column(String)
    admin_id = Column(Integer, ForeignKey('admin_infos.id'), unique=True)
    admin = relationship("AdminInfos", back_populates="credentials")
