from dataclasses import dataclass

@dataclass(frozen=True)
class Abbreviation:

    abbreviation : str

    def __post_init__(self):
        abbreviation = self.abbreviation.strip()

        if not abbreviation :
            raise ValueError("略称は必須です")
        
        object.__setattr__(self, "abbreviation", abbreviation)
        