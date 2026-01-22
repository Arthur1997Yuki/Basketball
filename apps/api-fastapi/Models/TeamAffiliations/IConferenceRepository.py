from abc import ABC, abstractmethod
from Models.TeamAffiliations.Conference import Conference

class IConferenceRepository(ABC) :

    @abstractmethod
    def add(self, conference : Conference) -> None :
        pass

    @abstractmethod
    def list(self) -> list[Conference] :
        pass

    @abstractmethod
    def get_by_id(self, conference_id : int) -> Conference | None :
        pass
