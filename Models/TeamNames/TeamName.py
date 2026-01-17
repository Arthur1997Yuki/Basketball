class TeamName:
    
    def __init__(self, name):
        if type(name) is not str:
            raise TypeError("引数が文字列ではありません")

        if len(name) == 0:
            raise ValueError("1文字以上である必要があります")
        
        self.name = name