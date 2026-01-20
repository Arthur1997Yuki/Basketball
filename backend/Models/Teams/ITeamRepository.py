from abc import ABC, abstractmethod
from backend.Models.Teams.Team import Team

class ITeamRepository(ABC) :

    @abstractmethod
    def add(home_town : Team) :
        pass

    @abstractmethod
    def list() -> list[Team] :
        pass