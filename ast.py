class Print():
    def __init__(self, value):
        self.value = value
        
    def eval(self):
        print(self.value.eval())

class Char_L():
    def __init__(self, value):
        self.value = value
        print("\n\n\nCHAR L : " + str(self.value))
        
    def eval(self):
        return(str(self.value))
