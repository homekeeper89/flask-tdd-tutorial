# coding: utf-8
from sqlalchemy import Column, DateTime, String, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class USERSTB(Base):
    __tablename__ = 'USERS_TB'

    IDX = Column(INTEGER(11), primary_key=True)
    NAME = Column(String(45))
    AGE = Column(TINYINT(4))
    HOBBY = Column(String(45))
    JOBS = Column(String(45))
    REGISTER_DATE = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
