from dataclasses import dataclass


@dataclass(frozen=True)
class DivisionName:

    name: str

    def __post_init__(self):
        normalized = self.name.strip()
        if not normalized:
            raise ValueError("ディビジョン名は必須です")
        object.__setattr__(self, "name", normalized)
