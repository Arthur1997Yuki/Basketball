from datetime import datetime
from backend.Models.TeamAffiliations.ConferenceName import ConferenceName

class Conference:

    conference_id: int
    name: str
    created_at: datetime | None

    def __init__(self, name: ConferenceName, conference_id=None, created_at=None):
        if conference_id is not None and not isinstance(conference_id, int):
            raise TypeError("カンファレンスIDは整数で指定してください。")
        if not isinstance(name, ConferenceName):
            raise TypeError("引数の型がカンファレンス名でありません")
        if not name:
            raise ValueError("カンファレンス名は必須です")

        self.conference_id = conference_id
        self.name = name.name
        self.created_at = created_at
    
