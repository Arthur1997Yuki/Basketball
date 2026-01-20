from dataclasses import dataclass

@dataclass(frozen=True)
class Conference:

    conference : str

    def __post_init__(self):
        if not self.conference :
            raise ValueError("カンファレンス名は必須です")