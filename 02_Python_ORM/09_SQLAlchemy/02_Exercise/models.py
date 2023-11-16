from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from decouple import config

DATABASE_URL = config('DATABASE_URL')
engine = create_engine(DATABASE_URL)

Base = declarative_base()


# Exam: 01. Model Recipe
class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True, unique=True, )
    name = Column(String, nullable=False, )
    ingredients = Column(Text, nullable=False, )
    instructions = Column(Text, nullable=False, )

    # Exam: 08.	Extend the Recipe Model
    chef_id = Column(Integer, ForeignKey('chefs.id'))
    chef = relationship("Chef", back_populates="recipes")


# Exam: 07.	Model Chef
class Chef(Base):
    __tablename__ = 'chefs'

    id = Column(Integer, primary_key=True, unique=True, )
    name = Column(String, nullable=False, )
    recipes = relationship('Recipe', back_populates='chef')
