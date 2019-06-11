class Util():
    def flat_list(self, lista):
        for i in lista: 
            if type(i) == list: 
                self.flat_list(i) 
            else: 
                self.out.append(i)
    
    def __init__(self,lista):
        self.lista = lista
        self.out = []
        self.flat_list(self.lista)
        
    
    def ret_out(self):
        return self.out
