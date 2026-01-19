from dataclasses import dataclass

@dataclass(frozen=True)
class Abbreviation:

    abbreviation : str

    def __init__(self, abbreviation):
        
        if not abbreviation :
            raise ValueError("略称は必須です")
        
        self.abbreviation = abbreviation

    @property
    def abbreviation(self) -> str :
        return self.abbreviation