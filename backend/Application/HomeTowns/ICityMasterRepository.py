from abc import ABC, abstractmethod


class ICityMasterRepository(ABC):
    @abstractmethod
    def get_city_names_by_pref2(self, pref2: str) -> set[str] | None:
        pass
