from fastapi import FastAPI
from app.routes import auth, workout

app = FastAPI()

# Register route modules
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(workout.router, prefix="/workouts", tags=["workouts"])
