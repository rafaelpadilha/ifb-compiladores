from rply import ParserGenerator
from ast import *

class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
        ['ID',  '<>',  '<=',  '>=',  '=',  '>',  '<',  'SOM',  'SUB',  'MUL',  'DIV',  'MOD',  'AND',  'OR',  'NOT',  'ATR',  'F_PAR',  'A_PAR',  'VIRG',  'PTV',  'A_CHA',  'F_CHA',  'IF',  'ELSE',  'WHILE',  'RETURN',  'FLOAT',  'CHAR',  'VOID',  'PRINT',  'INT',  'PROC',  'VAR',    'FLOAT',   'INT', 'FLOAT_L', 'INT_L', 'CHAR_L']
        )
        
    def parse(self):
        @self.pg.production('programa : decl_global')
        def programa(p):
            print("\nPROG")
            print(p)
        @self.pg.production('decl_global : decl_variavel')
        @self.pg.production('decl_global : decl_funcao')
        def decl_global(p):
            print("\nDECL_GL")
            print(p)
        @self.pg.production('decl_variavel : VAR lista_idents SUB tipo PTV')
        def decl_variavel(p):
            print("\nDECL_VAR")
            print(p)
        @self.pg.production('lista_idents : ID')
        def lista_idents(p):
            print("\nLISTA_IDENTS")
            print(p)
        @self.pg.production('tipo : INT')
        @self.pg.production('tipo : CHAR')
        @self.pg.production('tipo : FLOAT')
        @self.pg.production('tipo : VOID')
        def tipo(p):
            print("\nTIPO")
            print(p)
        @self.pg.production('decl_funcao : PROC nome_args SUB tipo bloco')
        @self.pg.production('decl_funcao : PROC nome_args bloco')
        def decl_funcao(p):
            print("\nDECL_FUNCAO")
            print(p)
        @self.pg.production('nome_args : ID A_PAR param_formais F_PAR')
        def nome_args(p):
            print("\nNOME_ARGS")
            print(p)
        @self.pg.production('param_formais : ID SUB tipo')
        @self.pg.production('param_formais : ')
        def param_formais(p):
            print("\nPARAM_FORM")
            print(p)
        @self.pg.production('bloco : A_CHA lista_comandos F_CHA ')
        def bloco(p):
            print("\nBLOCO")
            print(p)
        @self.pg.production('lista_comandos : comando lista_comandos')
        @self.pg.production('lista_comandos : ')
        def lista_comandos(p):
            print("\nLISTA_CMD")
            print(p)
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
        @self.pg.production('chamada_func_cmd : chamada_func PTV')
        def chamada_func_cmd(p):
            print("\nCHAM_FUN_CMD")
            print(p)
        @self.pg.production('retorno : RETURN exp PTV')
        def retorno(p):
            print("\nRETORNO")
            print(p)
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
            return(p[0])
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
            return(p[0])
        
        @self.pg.error
        def error_handle(token):
            raise ValueError(token)
            
            
    def get_parser(self):
        return self.pg.build()

