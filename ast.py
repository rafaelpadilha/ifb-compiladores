class Prog():
    def __init__(self, lista):
        self.lista = lista
        
    def eval(self):
        for cmd in self.lista:
            cmd.eval()

#Print
class Print():
    def __init__(self, value):
        self.value = value
        
    def eval(self):
        print(self.value.eval())
        
#Operacoes
class OpBin():
    def __init__(self, left, right):
        self.left = left
        self.right = right
        
class Som(OpBin):
    def eval(self):
        return self.left.eval() + self.right.eval()
        
class Sub(OpBin):
    def eval(self):
        return self.left.eval() - self.right.eval()
        
class Mul(OpBin):
    def eval(self):
        return self.left.eval() * self.right.eval()
        
class Div(OpBin):
    def eval(self):
        return self.left.eval() / self.right.eval()
        
class Mod(OpBin):
    def eval(self):
        return self.left.eval() % self.right.eval()
        
class And(OpBin):
    def eval(self):
        return self.left.eval() and self.right.eval()
        
class Or(OpBin):
    def eval(self):
        return self.left.eval() or self.right.eval()
        
class Igual(OpBin):
    def eval(self):
        if self.left.eval() is self.right.eval():
            return 1
        else:
            return 0

class Dif(OpBin):
    def eval(self):
        if self.left.eval() is not self.right.eval():
            return 1
        else:
            return 0

class Menor_Igual(OpBin):
    def eval(self):
        if self.left.eval() <= self.right.eval():
            return 1
        else:
            return 0

class Menor(OpBin):
    def eval(self):
        if self.left.eval() < self.right.eval():
            return 1
        else:
            return 0
            
class Maior_Igual(OpBin):
    def eval(self):
        if self.left.eval() >= self.right.eval():
            return 1
        else:
            return 0
            
class Maior(OpBin):
    def eval(self):
        if self.left.eval() > self.right.eval():
            return 1
        else:
            return 0
            
class Not():
    def __init__(self, value):
        self.value = value
        
    def eval(self):
        return int(not self.value.eval())
        
class Traco():
    def __init__(self, value):
        self.value = value
        
    def eval(self):
        return -self.value
    
class Identificador():
    def __init__(self, name, tipo, value=None):
        self.tipo = tipo
        self.name = name
        if tipo == 'INT' and value == None:
            self.value = 0
        elif tipo == 'FLOAT' and value == None:
            self.value = 0.0
        elif tipo == 'CHAR' and value == None:
            self.value = ''
        else:
            self.value = value
        
    def eval(self):
        return self.value
        
    def addr():
        return self
        
        
#Literais
class Int_L():
    def __init__(self, value):
        self.value = value
        
    def eval(self):
        return(int(self.value))
        
class Float_L():
    def __init__(self, value):
        tmp = str(value).replace(',','.')
        self.value = float(tmp)
        
    def eval(self):
        return(float(self.value))

class Char_L():
    def __init__(self, value):
        self.value = value
        
    def eval(self):
        return(str(self.value))
