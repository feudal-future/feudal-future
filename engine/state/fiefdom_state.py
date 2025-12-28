from pydantic import BaseModel, Field

class FiefdomState(BaseModel):
    id: str = Field(..., alias="_id")
    version: int = 0
    resources: ResourcesState
    hamlets: HamletsState

class ResourcesState(BaseModel):
    food: int
    wood: int
    iron: int

class HamletsState(BaseModel):
    level: int
    villagers: int
