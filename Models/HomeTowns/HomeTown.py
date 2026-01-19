from dataclasses import dataclass
import Prefecture
import City

@dataclass(frozen=True)
class HomeTown:

    prefecture : Prefecture.Prefecture
    city : City.City

    def __init__(self, prefecture, city):
        if not isinstance(prefecture, Prefecture.Prefecture):
            raise TypeError("引数の型が都道府県でありません")
        if not isinstance(city, City.City):
            raise TypeError("引数の型が市区町村でありません")
        self.prefecture = prefecture
        self.city = city

    @property
    def hometown(self) -> str:
        return self.prefecture.prefecture + self.city.city
