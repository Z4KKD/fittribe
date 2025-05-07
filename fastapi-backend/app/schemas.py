from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    email: str
    name: str
    bio: str = None
    avatar: str = None
    fitness_goals: str = None

class UserCreate(UserBase):
    password: str

class UserLogin(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        from_attributes = True


class WorkoutBase(BaseModel):
    workout_type: str
    duration: float
    intensity: str
    notes: Optional[str] = None

class WorkoutCreate(WorkoutBase):
    pass

class Workout(WorkoutBase):
    id: int
    user_id: int
    date: datetime

    class Config:
        from_attributes = True