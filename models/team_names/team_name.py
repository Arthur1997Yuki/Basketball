class team_name:
    def __init__(self, name):
        if len(name) == 0:
            raise ValueError("1文字以上である必要があります")
        self.name = name