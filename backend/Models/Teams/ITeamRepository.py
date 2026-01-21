from abc import ABC, abstractmethod
from backend.Models.Teams.Team import Team

class ITeamRepository(ABC) :

    @abstractmethod
    def add(self, team : Team) -> None :
        pass

    @abstractmethod
    def list(self) -> list[Team] :
        pass
