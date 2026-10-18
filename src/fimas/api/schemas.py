from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    status: str = "ok"


class AllocationRequest(BaseModel):
    supply: float = Field(ge=0)
    demands: dict[str, float]
