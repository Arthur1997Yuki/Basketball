from dataclasses import dataclass

@dataclass(frozen=True)
class ManagementCorporation:

    management_corporation : str

    def __init__(self, management_corporation : str):
        if not management_corporation:
            raise ValueError("正式名称は必須です")
        
        self.management_corporation = management_corporation
