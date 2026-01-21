from dataclasses import dataclass

@dataclass(frozen=True)
class SeasonName:
    
    season_name : str

    def __post_init__(self):
        season_name = self.season_name.strip()

        if not season_name :
            raise ValueError("シーズン名称は必須です")