from dataclasses import dataclass

@dataclass(frozen=True)
class Division:

    division : str

    def __post_init__(self):
        if not self.division :
            raise ValueError("ディビジョン名は必須です")    
    