from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class Season:

    season_name : str
    start_date : date
    end_date : date

    def __post_init__(self):
        pass