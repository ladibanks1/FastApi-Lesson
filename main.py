from fastapi import FastAPI, Depends
from app import Base, engine, UserSchema, db_session, User
from sqlalchemy.orm import Session


# Fast Api Instance
app = FastAPI()
Base.metadata.create_all(bind=engine)


# Api Endpints
@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/")
def create_user(user: UserSchema, session: Session = Depends(db_session)):
    user: User = User(
        first_name=user.first_name, last_name=user.last_name, age=user.age
    )
    session.add(user)
    session.commit()
    return {"message": "User Created ", "data": user.to_dict()}
