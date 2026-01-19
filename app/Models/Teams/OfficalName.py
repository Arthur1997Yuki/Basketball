from dataclasses import dataclass

@dataclass(frozen=True)
class OfficalName:
    
    offical_name : str

    def __init__(self, offical_name : str):

        if not offical_name :
            raise ValueError("正式名称は必須です")

        self.offical_name = offical_name

    @property
    def offical_name(self) -> str:
        return self.offical_name