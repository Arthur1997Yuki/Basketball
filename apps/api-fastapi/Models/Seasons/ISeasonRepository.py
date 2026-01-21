from abc import ABC, abstractmethod
from Models.Seasons.Season import Season

class ISeasonRepository(ABC) :

    @abstractmethod
    def add(self, season : Season) -> None :
        pass

    @abstractmethod
    def list(self) -> list[Season] :
        pass
