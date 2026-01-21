from dataclasses import dataclass

@dataclass(frozen=True)
class ManagementCorporation:

    management_corporation : str

    def __post_init__(self) -> None:
        management_corporation = self.management_corporation.strip()
        
        if not management_corporation:
            raise ValueError("運営法人は必須です")
        
        object.__setattr__(self, "management_corporation", management_corporation)