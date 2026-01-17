class Result:
    
    def __init__(self, result):
        if type(result) is  not bool:
            raise TypeError("引数が真偽値ではありません")
        
        self.result = result