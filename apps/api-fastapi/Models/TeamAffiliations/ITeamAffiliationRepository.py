from abc import ABC, abstractmethod
from Models.TeamAffiliations.TeamAffiliation import TeamAffiliation

class ITeamAffiliationRepository(ABC) :

    @abstractmethod
    def add(self, team_affiliation : TeamAffiliation) -> None :
        pass

    @abstractmethod
    def list(self) -> list[TeamAffiliation] :
        pass