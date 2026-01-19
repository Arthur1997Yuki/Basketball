from dataclasses import dataclass
import Prefecture
import City

@dataclass(frozen=True)
class HomeTown:

    prefecture : Prefecture
    city : City

    def __init__(self, prefecture, city):
        self.prefecture = prefecture
        self.city = city

    @property
    def hometown(self) -> str:
        return self.prefecture.prefecture + self.city.city