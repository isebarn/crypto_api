import os
import json
from datetime import datetime
from sqlalchemy import ForeignKey, desc, create_engine, func, Column, BigInteger, Integer, Float, String, Boolean, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from werkzeug.security import generate_password_hash, check_password_hash

engine = create_engine(os.environ.get('DATABASE'), echo=False)
Base = declarative_base()

def json_object(_object):
  data = dict(_object.__dict__)
  data.pop('_sa_instance_state', None)
  return data

def json_child_list(data, name):
  if name in data:
    data[name] = [_object.json() for _object in data[name]]

def json_child_object(data, name):
  if name in data:
    data[name] = data[name].json()

class Game(Base):
  __tablename__ = 'games'

  Id = Column('id', Integer, primary_key=True)
  UserId = Column('user_id', Integer, ForeignKey('users.id'))
  Path = Column('path', String)
  Icon = Column('icon', String)
  Name = Column('name', String)
  Github = Column('github', String)
  Active = Column('active', Boolean)


  def __init__(self, data):
    self.UserId = data['user_id']
    self.Icon = data['icon']
    self.Name = data['name']
    self.Github = data['github']
    self.Active = False

  def json(self):
    data = json_object(self)
    return data

class User(Base):
  __tablename__ = 'users'

  Id = Column('id', Integer, primary_key=True)
  Name = Column('name', String)
  Email = Column('email', String, unique=True)
  Password = Column('password', String)
  Developer = Column('developer', Boolean)

  def __init__(self, data):
    self.Email = data['email']
    self.Name = data['name']
    self.Password = generate_password_hash(data['password'], method='sha256')
    self.Developer = data.get('developer', False)

  def json(self):
    data = json_object(self)
    return data


class Operations:
  def SaveGame(data):
    if session.query(Game.Id).filter_by(Name=data['name']).scalar() == None:
      session.add(Game(data))
      session.commit()

  def QueryGames():
    return [x.json() for x in session.query(Game).all()]

  def QueryDeveloperGames(developer_id):
    return [x.json() for x in session.query(Game).filter_by(UserId=int(developer_id))]


  def SaveUser(data):
    session.add(User(data))
    session.commit()

  def Login(data):
    user = session.query(User).filter_by(Email=data['Username']).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.Password, data['Password']):
      raise Exception("Invalid email or password")

    return user.json()


Base.metadata.create_all(engine)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

if __name__ == "__main__":
  print(os.environ.get('DATABASE'))