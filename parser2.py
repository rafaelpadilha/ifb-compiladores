from rply import ParserGenerator
from ast import *

class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
        ['ID',  '<>',  '<=',  '>=',  '=',  '>',  '<',  'SOM',  'SUB',  'MUL',  'DIV',  'MOD',  'AND',  'OR',  'NOT',  'ATR',  'F_PAR',  'A_PAR',  'VIRG',  'PTV',  'A_CHA',  'F_CHA',  'IF',  'ELSE',  'WHILE',  'RETURN',  'FLOAT',  'CHAR',  'VOID',  'PRINT',  'INT',  'PROC',  'VAR',    'FLOAT',   'INT', 'FLOAT_L', 'INT_L', 'CHAR_L']
        )
        self.ids = {}
        self.list_cmds = []
        
    def parse(self):
        @self.pg.production('programa : decl_global')
        @self.pg.production('programa : decl_global programa')
        @self.pg.production('programa : ')
        def programa(p):
            print("\nPROG")
            print(p)

            print("\n\nSaida >> ")
            if len(p)>0:
                return Prog(p[0])
        @self.pg.production('decl_global : decl_variavel')
        @self.pg.production('decl_global : decl_funcao')
        def decl_global(p):
            print("\nDECL_GL")
            print(p)
            return(p[0])
        @self.pg.production('decl_variavel : VAR lista_idents SUB tipo PTV')
        def decl_variavel(p):
            print("\nDECL_VAR")
            print(p)
            for id in p[1]:
                if id <> None:
                    self.ids[id.value]=Identificador(p[1],p[3])
            print(self.ids)
        @self.pg.production('lista_idents : ID prod1')
        def lista_idents(p):
            print("\nLISTA_IDENTS")
            print(p)
            l_id = [p[0]]
            if p[1] <> None:
                for i in p[1]:
                    l_id.append(i)

            for id in l_id:
                if id not in self.ids:
                    self.ids[id.value]=None
                else:
                    print("ID \" " + id + " \" ja declarado")
                return l_id
                
        #PROD1 ADD
        @self.pg.production('prod1 : VIRG ID prod1')
        @self.pg.production('prod1 : VIRG ID')
        @self.pg.production('prod1 : ')
        def prod1(p):
            print("\nPROD1")
            print(p)
            if len(p)>0:
                if p[2] == None:
                    return p[1]
                else:
                    if type(p[2])==list:
                        ret = [p[1]]
                        for i in p[2]:
                            ret.append(i)
                        return ret
                    else:
                        return(list([p[1],p[2]]))
                
        #END PROD1
        @self.pg.production('tipo : INT')
        @self.pg.production('tipo : CHAR')
        @self.pg.production('tipo : FLOAT')
        @self.pg.production('tipo : VOID')
        def tipo(p):
            print("\nTIPO")
            print(p)
            return(p[0])
        @self.pg.production('decl_funcao : PROC nome_args SUB tipo bloco')
        @self.pg.production('decl_funcao : PROC nome_args bloco')
        def decl_funcao(p):
            print("\nDECL_FUNCAO")
            print(p)
            if(len(p)==5):
                return(p[4])
            else:
                return(p[2])
        @self.pg.production('nome_args : ID A_PAR param_formais F_PAR nome_args')
        @self.pg.production('nome_args : ID A_PAR param_formais F_PAR ')
        def nome_args(p):
            print("\nNOME_ARGS")
            print(p)
            
        #PROD2 ADD
        #@self.pg.production('prod2 : ID A_PAR param_formais F_PAR prod2')
        #@self.pg.production('prod2 : ')
        #END
        @self.pg.production('param_formais : ID SUB tipo')
        @self.pg.production('param_formais : ')
        def param_formais(p):
            print("\nPARAM_FORM")
            print(p)
        @self.pg.production('bloco : A_CHA lista_comandos F_CHA ')
        def bloco(p):
            print("\nBLOCO")
            print(p)
            return(p[1])
        @self.pg.production('lista_comandos : comando lista_comandos')
        @self.pg.production('lista_comandos : ')
        def lista_comandos(p):
            print("\nLISTA_CMD")
            print(p)
            if(len(p)>0):
                return(self.list_cmds)
        @self.pg.production('comando : decl_variavel')
        @self.pg.production('comando : atribuicao')
        @self.pg.production('comando : iteracao')
        @self.pg.production('comando : decisao')
        @self.pg.production('comando : escrita')
        @self.pg.production('comando : retorno')
        @self.pg.production('comando : bloco')
        @self.pg.production('comando : chamada_func_cmd')
        def comando(p):
            print("\nCOMANDOOOOO")
            print(p)
            if p[0] <> None:
                self.list_cmds.append(p[0])
                print("##LISTA CMD" + str(self.list_cmds))
                return(p[0])
        @self.pg.production('atribuicao : ID ATR exp PTV')
        def atribuicao(p):
            print("\nAAAAAAAAAAAAAAAATR")
            print(p)
        @self.pg.production('iteracao : WHILE A_PAR exp F_PAR PTV')
        def iteracao(p):
            print("\nITERACAO")
            print(p)
        @self.pg.production('decisao : IF A_PAR exp F_PAR comando ELSE comando')
        @self.pg.production('decisao : IF A_PAR exp F_PAR comando')
        def decisao(p):
            print("\nDECISAO")
            print(p)
        @self.pg.production('escrita : PRINT A_PAR lista_exprs F_PAR PTV')
        def escrita(p):
            print("\nESCRITAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            print(p)
            return Print(p[2])
        @self.pg.production('chamada_func_cmd : chamada_func PTV')
        def chamada_func_cmd(p):
            print("\nCHAM_FUN_CMD")
            print(p)
        @self.pg.production('retorno : RETURN exp PTV')
        def retorno(p):
            print("\nRETORNO")
            print(p)
            return p[1]
        @self.pg.production('chamada_func : ID A_PAR lista_exprs F_PAR')
        def chamada_func(p):
            print("\nCHAMADA_FUNC")
            print(p)
        @self.pg.production('lista_exprs : ')
        @self.pg.production('lista_exprs : exp')
        def lista_exprs(p):
            print("\nLISTA_EXPS")
            print(p)
            return(p[0])
        @self.pg.production('exp : exp SOM exp')
        @self.pg.production('exp : exp SUB exp')
        @self.pg.production('exp : exp MUL exp')
        @self.pg.production('exp : exp DIV exp')
        @self.pg.production('exp : exp MOD exp')
        @self.pg.production('exp : exp AND exp')
        @self.pg.production('exp : exp OR exp')
        @self.pg.production('exp : exp = exp')
        @self.pg.production('exp : exp <> exp')
        @self.pg.production('exp : exp <= exp')
        @self.pg.production('exp : exp < exp')
        @self.pg.production('exp : exp >= exp')
        @self.pg.production('exp : exp > exp')
        @self.pg.production('exp : expr_basica')
        def exp(p):
            print("\nEXP")
            print(p)
            if(len(p)==1):
                return(p[0])
            elif(len(p)==3):
                if p[1].gettokentype() == 'SOM':
                    return Som(p[0],p[2])
                elif p[1].gettokentype() == 'SUB':
                    return Sub(p[0],p[2])
                elif p[1].gettokentype() == 'MUL':
                    return Mul(p[0],p[2])
                elif p[1].gettokentype() == 'DIV':
                    return Div(p[0],p[2])
                elif p[1].gettokentype() == 'MOD':
                    return Mod(p[0],p[2])
                elif p[1].gettokentype() == 'AND':
                    return And(p[0],p[2])
                elif p[1].gettokentype() == 'OR':
                    return Or(p[0],p[2])
                elif p[1].gettokentype() == '=':
                    return Igual(p[0],p[2])
                elif p[1].gettokentype() == '<>':
                    return Dif(p[0],p[2])
                elif p[1].gettokentype() == '<=':
                    return Menor_Igual(p[0],p[2])
                elif p[1].gettokentype() == '<':
                    return Menor(p[0],p[2])
                elif p[1].gettokentype() == '>=':
                    return Maior_Igual(p[0],p[2])
                elif p[1].gettokentype() == '>':
                    return Maior(p[0],p[2])
                
        @self.pg.production('expr_basica : A_PAR exp F_PAR')
        @self.pg.production('expr_basica : NOT expr_basica')
        @self.pg.production('expr_basica : SUB expr_basica')
        @self.pg.production('expr_basica : INT_L')
        @self.pg.production('expr_basica : CHAR_L')
        @self.pg.production('expr_basica : FLOAT_L')
        @self.pg.production('expr_basica : ID')
        @self.pg.production('expr_basica : chamada_func')
        def expr_basica(p):
            print("\nEXP_BAS")
            print(p)
            if len(p)==3:
                return(p[1])
            elif len(p)==2:
                if p[0].gettokentype() == 'NOT':
                    return Not(p[1])
                elif p[0].gettokentype() == 'SUB':
                    return Traco(p[1])
                    
            elif len(p)==1:
                if p[0].gettokentype() == 'CHAR_L':
                    return Char_L(p[0].value)
                elif p[0].gettokentype() == 'INT_L':
                    return Int_L(p[0].value)
                elif p[0].gettokentype() == 'FLOAT_L':
                    return Float_L(p[0].value)
                elif p[0].gettokentype() == 'ID':
                    if p[0].value in self.ids:
                        return self.ids[p[0].value]
                    else:
                        print("ID nao declarado.")
        
        @self.pg.error
        def error_handle(token):
            raise ValueError(token)
            
            
    def get_parser(self):
        return self.pg.build()

