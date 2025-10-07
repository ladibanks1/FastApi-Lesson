from pydantic import BaseModel, Field


class User(BaseModel):
    first_name: str = Field(min_length=1)
    last_name: str = Field(min_length=1)
    age: int = Field(gt=14, lt=30)
