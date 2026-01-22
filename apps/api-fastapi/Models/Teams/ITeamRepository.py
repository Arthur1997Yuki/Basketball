from abc import ABC, abstractmethod
from Models.Teams.Team import Team

class ITeamRepository(ABC) :

    @abstractmethod
    def add(self, team : Team) -> None :
        pass

    @abstractmethod
    def list(self) -> list[Team] :
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Team | None :
        pass