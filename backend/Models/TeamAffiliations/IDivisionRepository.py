from abc import ABC, abstractmethod
from backend.Models.TeamAffiliations.Division import Division

class IDivisionRepository(ABC) :

    @abstractmethod
    def add(home_town : Division) :
        pass

    @abstractmethod
    def list() -> list[Division] :
        pass