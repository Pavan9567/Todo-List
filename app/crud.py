from sqlalchemy.orm import Session
from . import models, schemas
from .auth import hash_password

def create_user(db: Session, user: schemas.UserCreate):
    hashed_pw = hash_password(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_todo(db: Session, todo: schemas.ToDoCreate, user_id: int):
    db_todo = models.ToDo(**todo.dict(), owner_id=user_id)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def get_todos(db: Session, user_id: int):
    return db.query(models.ToDo).filter(models.ToDo.owner_id == user_id).all()
