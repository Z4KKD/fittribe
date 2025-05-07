from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

router = APIRouter()

@router.post("/workout")
def log_workout(workout: dict):
    return {"message": "Workout logged successfully"}

@router.post("/workouts/", response_model=schemas.Workout)
def create_workout(workout: schemas.WorkoutCreate, db: Session = Depends(get_db), user_id: int = 1):
    return crud.create_workout(db=db, workout=workout, user_id=user_id)

@router.get("/workouts/", response_model=list[schemas.Workout])
def get_workouts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), user_id: int = 1):
    return crud.get_workouts(db=db, user_id=user_id, skip=skip, limit=limit)
