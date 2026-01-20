from dataclasses import dataclass
from backend.Models.HomeTowns.Prefecture import Prefecture


@dataclass(frozen=True)
class City:

    prefecture : Prefecture
    city : str

    def __post_init__(self):

        prefecture = self.prefecture
        city = self.city.strip()
        
        if not isinstance(prefecture, Prefecture):
            raise TypeError("引数の型が都道府県でありません")
        
        if not city:
            raise ValueError("市区町村名は必須です。")

        object.__setattr__(self, "prefecture", prefecture)
        object.__setattr__(self, "city", city)
