from abc import ABC, abstractmethod
from Models.TeamAffiliations.Division import Division

class IDivisionRepository(ABC) :

    @abstractmethod
    def add(self, division : Division) -> None :
        pass

    @abstractmethod
    def list(self) -> list[Division] :
        pass

    @abstractmethod
    def get_by_id(self, division_id : int) -> Division | None :
        pass