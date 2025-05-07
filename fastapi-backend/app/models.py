from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    name = Column(String)
    bio = Column(String, nullable=True)
    avatar = Column(String, nullable=True)
    fitness_goals = Column(String, nullable=True)

class Workout(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    workout_type = Column(String, index=True)
    duration = Column(Float)  # in minutes
    intensity = Column(String)
    notes = Column(String, nullable=True)
    date = Column(DateTime, default=datetime.utcnow)

    # Calculate XP based on the workout type and intensity
    def calculate_xp(self):
        xp_multiplier = {
            "Running": {"Low": 10, "Medium": 20, "High": 30},
            "Cycling": {"Low": 8, "Medium": 16, "High": 24},
            "Weights": {"Low": 12, "Medium": 24, "High": 36},
            "Yoga": {"Low": 5, "Medium": 10, "High": 15},
        }
        return xp_multiplier.get(self.workout_type, {}).get(self.intensity, 0)
