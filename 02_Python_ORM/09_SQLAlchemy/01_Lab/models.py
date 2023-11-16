from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from decouple import config

DATABASE_URL = config('DATABASE_URL')
engine = create_engine(DATABASE_URL)

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    is_completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User')


# Create tables in the database (no migrations management)
# Base.metadata.create_all(engine)
