from datetime import datetime
from backend.Models.TeamAffiliations.DivisionName import DivisionName


class Division:

    division_id: int
    name: str
    created_at: datetime | None

    def __init__(self, name: DivisionName | str, division_id=None, created_at=None):
        if division_id is not None and not isinstance(division_id, int):
            raise TypeError("ディビジョンIDは整数で指定してください。")
        if isinstance(name, DivisionName):
            name = name.name
        if not name:
            raise ValueError("ディビジョン名は必須です")
        self.division_id = division_id
        self.name = name
        self.created_at = created_at
    
