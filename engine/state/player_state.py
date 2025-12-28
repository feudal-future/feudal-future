from pydantic import BaseModel, Field

class PlayerState(BaseModel):
    id: str = Field(..., alias="_id")
    name: str