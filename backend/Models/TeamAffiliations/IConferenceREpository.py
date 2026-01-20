from abc import ABC, abstractmethod
from backend.Models.TeamAffiliations.Conference import Conference

class IConferenceRepository(ABC) :

    @abstractmethod
    def add(conference : Conference) :
        pass

    @abstractmethod
    def list() -> list[Conference] :
        pass