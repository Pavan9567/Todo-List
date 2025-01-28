from fastapi import FastAPI
from .routes import todos, users

app = FastAPI()

app.include_router(users.router, prefix="/api", tags=["Users"])
app.include_router(todos.router, prefix="/api", tags=["To-Dos"])

@app.get("/")
def root():
    return {"message": "Welcome to To-Do API"}
