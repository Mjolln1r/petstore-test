from pydantic import BaseModel


class Pet(BaseModel):
    id: int
    category: dict
