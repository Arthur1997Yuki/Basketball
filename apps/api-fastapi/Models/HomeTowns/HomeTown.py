from dataclasses import dataclass
from Models.HomeTowns.Prefecture import Prefecture
from Models.HomeTowns.City import City

@dataclass(frozen=True)
class HomeTown:

    prefecture : Prefecture
    city : City

    def __post_init__(self):
        
        prefecture = self.prefecture
        city = self.city
        
        if not isinstance(prefecture, Prefecture):
            raise TypeError("引数の型が都道府県でありません")
        if not isinstance(city, City):
            raise TypeError("引数の型が市区町村でありません")
        
        object.__setattr__(self, "prefecture", prefecture)
        object.__setattr__(self, "city", city)

    @property
    def hometown(self) -> str:
        return self.prefecture.prefecture + self.city.city
