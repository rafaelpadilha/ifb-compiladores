from rply import ParserGenerator
from ast import *

class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
        ['ID',  '<>',  '<=',  '>=',  '=',  '>',  '<',  'SOM',  'SUB',  'MUL',  'DIV',  'MOD',  'AND',  'OR',  'NOT',  'ATR',  'F_PAR',  'A_PAR',  'VIRG',  'PTV',  'A_CHA',  'F_CHA',  'IF',  'ELSE',  'WHILE',  'RETURN',  'FLOAT',  'CHAR',  'VOID',  'PRINT',  'INT',  'PROC',  'VAR',    'FLOAT',   'INT', 'FLOAT_L', 'INT_L', 'CHAR_L']
        )
        
    def parse(self):
        @self.pg.production('programa : prod_prog')
	def programa():
		return (self)
	@self.pg.production('prod_prog : ')
	@self.pg.production('prod_prog : decl_global prod_prog')
	def prod_prog(p):
		print(p)
	@self.pg.production('decl_global : decl_variavel')
        @self.pg.production('decl_global : decl_funcao')
        @self.pg.production('decl_variavel : VAR lista_idents SUB tipo PTV')
        @self.pg.production('lista_idents : ID mais_idents')
	@self.pg.production('mais_idents : ')
	@self.pg.production('mais_idents : VIRG ID mais_idents')
        @self.pg.production('tipo : INT')
        @self.pg.production('tipo : CHAR')
        @self.pg.production('tipo : FLOAT')
	@self.pg.production('tipo : VOID')
        @self.pg.production('decl_funcao : PROC nome_args SUB tipo bloco')
        @self.pg.production('decl_funcao : PROC nome_args bloco')
        @self.pg.production('nome_args : ID A_PAR param_formais F_PAR nome_args_p')
        @self.pg.production('nome_args_p : ID A_PAR param_formais F_PAR nome_args_p')
	@self.pg.production('nome_args_p : ')
        @self.pg.production('param_formais : ID SUB tipo prod1')
        @self.pg.production('param_formais : ')
	@self.pg.production('prod1 : VIRG ID SUB tipo prod1')
	@self.pg.production('prod1 : ')
        @self.pg.production('bloco : A_CHA lista_comandos F_CHA ')
        @self.pg.production('lista_comandos : comando lista_comandos')
	@self.pg.production('lista_comandos : ')
        @self.pg.production('comando : decl_variavel')
        @self.pg.production('comando : atribuicao')
        @self.pg.production('comando : iteracao')
        @self.pg.production('comando : decisao')
        @self.pg.production('comando : escrita')
        @self.pg.production('comando : retorno')
        @self.pg.production('comando : bloco')
        @self.pg.production('comando : chamada_func_cmd')
        @self.pg.production('atribuicao : ID ATR exp PTV')
        @self.pg.production('iteracao : WHILE A_PAR exp F_PAR PTV')
        @self.pg.production('decisao : IF A_PAR exp F_PAR comando ELSE comando')
        @self.pg.production('decisao : IF A_PAR exp F_PAR comando')
        @self.pg.production('escrita : PRINT A_PAR lista_exprs F_PAR PTV')
	def escrita(p):
		print(p)
		return Print(p)
        @self.pg.production('chamada_func_cmd : chamada_func PTV')
        @self.pg.production('retorno : RETURN exp PTV')
        @self.pg.production('chamada_func : ID A_PAR lista_exprs F_PAR prod2')
	@self.pg.production('prod2 : ID A_PAR lista_exprs F_PAR')
	@self.pg.production('prod2 : ')
        @self.pg.production('lista_exprs : ')
        @self.pg.production('lista_exprs : exp prod3')
	@self.pg.production('prod3 : VIRG exp prod3')
	@self.pg.production('prod3 : ')
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
        @self.pg.production('expr_basica : A_PAR exp F_PAR')
        @self.pg.production('expr_basica : NOT expr_basica')
        @self.pg.production('expr_basica : SUB expr_basica')
        @self.pg.production('expr_basica : INT_L')
        @self.pg.production('expr_basica : CHAR_L')
        @self.pg.production('expr_basica : FLOAT_L')
        @self.pg.production('expr_basica : ID')
        @self.pg.production('expr_basica : chamada_func')
        
        @self.pg.error
        def error_handle(token):
            raise ValueError(token)
            
            
    def get_parser(self):
        return self.pg.build()

