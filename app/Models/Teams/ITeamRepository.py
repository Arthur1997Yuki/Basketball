from abc import ABC, abstractmethod
import Team

class ITeamRepository(ABC) :

    @abstractmethod
    def save(home_town : Team.Team) :
        pass