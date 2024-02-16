from datetime import datetime

class LineAPILogger():
    def __init__(self):
        self.filename = datetime.now().strftime("%m_%d_%H_%M") + "log.txt"
        with open(self.filename, "w") as f:
            f.write(self.filename)
        
    def log(self, text:str, level:int = 0):
        message = "\t"*level
        message += text + "\n"
        with open(self.filename, "a") as f:
            f.write(text)
    