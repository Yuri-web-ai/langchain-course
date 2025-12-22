from typing import List

from pydantic import BaseModel, Field

class Source(BaseModel):
    """Schema representing a source entity."""
    #id: str = Field(..., description="Unique identifier for the source")
    #name: str = Field(..., description="Name of the source")
    url: str = Field(description="URL of the source")

class AgentResponse(BaseModel):
    """Schema representing the response from an agent."""
    answer: str = Field(description="The main answer provided by the agent")
    sources: List[Source] = Field(
        default_factory=list, description="List of sources used to generate the answer"
    )

