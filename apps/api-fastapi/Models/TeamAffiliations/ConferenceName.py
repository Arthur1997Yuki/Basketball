from dataclasses import dataclass

@dataclass(frozen=True)
class ConferenceName:

    name : str

    def __post_init__(self):
        if not self.name :
            raise ValueError("カンファレンス名は必須です")