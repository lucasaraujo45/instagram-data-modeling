import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    __password = Column(String(20), nullable=False)
    dob = Column(String(250), nullable=False)

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    photo = Column(String(250), nullable=False)
    post_name = Column(String(250), nullable=False)
    comments = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Story(Base):
    __tablename__ = 'story'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    video_photo = Column(String(250), nullable=False)
    story_name = Column(String(250), nullable=False)
    comments = Column(String(250), nullable=False)
    story_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Feed(Base):
    __tablename__ = 'feed'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    feed_stories = Column(String(250), nullable=False)
    feed_posts = Column(String(250), nullable=False)
    feed_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    def to_dict(self):
        return {}


# class User(Base):
#     __tablename__ = 'user'
#     id = Column(Integer, primary_key=True)
#     user_name = Column(String(250))
#     email_adress = Column(String(250))
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}
    
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')