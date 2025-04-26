from pydantic import BaseModel
from typing import List

class Container(BaseModel):
    id: str
    origin: str
    destination: str
    weight: float

class Route(BaseModel):
    from_node: str
    to_node: str
    cost: float

class InputData(BaseModel):
    containers: List[Container]
    routes: List[Route]

class MovePlan(BaseModel):
    containerId: str
    route: List[str]
    totalCost: float

class OutputData(BaseModel):
    plan: List[MovePlan]
    latencyMs: float
