from abc import ABC, abstractmethod
import Team

class ITeamRepository(ABC) :

    @abstractmethod
    def add(home_town : Team.Team) :
        pass