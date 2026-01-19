from abc import ABC, abstractmethod
import HomeTown

class IHomeTownRepository(ABC) :

    @abstractmethod
    def save(home_town : HomeTown.HomeTown) :
        pass

    