class Prog():
    def __init__(self, lista):
        self.lista = lista
        
    def eval(self):
        print("EVAL<"+str(self.lista))
        if(type(self.lista) == list):
            for func in self.lista:
                if func != None and isinstance(func,Func) and func.nome == 'main':
                    func.eval()
        else:
            self.lista.eval()  
                  
class Func():
    def __init__(self, nome, cmds, param ,tipo='Void'):
        self.cmds = cmds
        self.nome = nome
        self.param = param
        self.tipo = tipo
        self.resultado = 0
        
    def eval(self, t_param=None):
        if t_param != None :
            if len(t_param) != len(self.param):
                err("Quantidade de parametros, nao equivalentes.")
            print("CMDS><" + str(self.cmds))
            if self.cmds != None:
                if(type(self.cmds) == list):
                    for i in self.cmds:
                        if i != None:
                            return i.eval(t_param)
                else:
                    return self.cmds.eval(t_param)
        else:
            if self.param == None:
                print("CMDS><" + str(self.cmds))
                if self.cmds != None:
                    if(type(self.cmds) == list):
                        for i in self.cmds:
                            if i != None:
                                return i.eval()
                    else:
                        return self.cmds.eval()
            else: 
                err("Quantidade de parametros, nao equivalentes.")

#Print
class Print():
    def __init__(self, value):
        self.value = value
        
    def eval(self):
        if isinstance(self.value, list):
            self.out=''
            for i in self.value:
                j = str(i.eval())
                self.out = self.out + j
            print(self.out)
        else:
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
        
    def atr(self,val):
        self.value = val
        
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
        res = self.value
        res = res.replace('\'','')
        return(str(res))
