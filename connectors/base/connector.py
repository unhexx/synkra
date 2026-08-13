"""Base Connector interface for Synkra (Airbyte CDK inspired)."""
from abc import ABC, abstractmethod
from typing import Any, Dict, Iterator, Optional
from pydantic import BaseModel

class ConnectorConfig(BaseModel):
    name: str
    version: str
    credentials: Dict[str, Any]
    # ... extend per system

class Source(ABC):
    @abstractmethod
    def check(self) -> bool:
        """Validate connection."""
        ...

    @abstractmethod
    def discover(self) -> Dict[str, Any]:
        """Return catalog of objects/classes/schemas."""
        ...

    @abstractmethod
    def read(self, catalog: Dict, state: Optional[Dict] = None) -> Iterator[Dict]:
        """Yield records (objects) with optional CDC state."""
        ...

class Destination(ABC):
    @abstractmethod
    def write(self, records: Iterator[Dict]) -> None:
        ...
