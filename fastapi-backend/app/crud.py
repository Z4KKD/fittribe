from sqlalchemy.orm import Session
from . import models, schemas
from . import auth
from datetime import datetime

def create_user(db: Session, user: schemas.UserCreate, hashed_password: str):
    db_user = models.User(
        email=user.email,
        password_hash=hashed_password,
        name=user.name,
        bio=user.bio,
        avatar=user.avatar,
        fitness_goals=user.fitness_goals
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_workout(db: Session, workout: schemas.WorkoutCreate, user_id: int):
    db_workout = models.Workout(
        user_id=user_id,
        workout_type=workout.workout_type,
        duration=workout.duration,
        intensity=workout.intensity,
        notes=workout.notes,
        date=datetime.utcnow()
    )
    db.add(db_workout)
    db.commit()
    db.refresh(db_workout)
    return db_workout

def get_workouts(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Workout).filter(models.Workout.user_id == user_id).offset(skip).limit(limit).all()
