from dataclasses import dataclass

@dataclass(frozen=True)
class OfficialName:

    official_name : str

    def __post_init__(self):
        official_name = self.official_name.strip()

        if not official_name :
            raise ValueError("正式名称は必須です")
        object.__setattr__(self, "official_name", official_name)