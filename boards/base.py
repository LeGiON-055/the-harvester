from abc import ABC, abstractmethod

class BoardAdapter(ABC):
    @abstractmethod
    def fetch(self, role: str, location: str) -> list[dict]:
        """Fetch job listings for the given role and location."""
        pass