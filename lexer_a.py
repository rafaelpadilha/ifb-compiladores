from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Operadores relacionais
        self.lexer.add('<>','<>')
        self.lexer.add('<=','<=')
        self.lexer.add('>=','>=')
        self.lexer.add('=','=')
        self.lexer.add('>','>')
        self.lexer.add('<','<')

        # Operadores logicosaritmeticos
        self.lexer.add('SOM',r'\+')
        self.lexer.add('SUB',r'\-')
        self.lexer.add('MUL',r'\*')
        self.lexer.add('DIV',r'\/')
        self.lexer.add('MOD',r'\%')
        self.lexer.add('AND',r'and')
        self.lexer.add('OR',r'or')
        self.lexer.add('NOT',r'not')

        # Atribuicao 
        self.lexer.add('ATR',r':=')

        #Simbolos especiais
        self.lexer.add('F_PAR',r'\)')
        self.lexer.add('A_PAR',r'\(')
        self.lexer.add('VIRG',r'\,')
        self.lexer.add('PTV',r'\;')
        self.lexer.add('A_CHA',r'\{')
        self.lexer.add('F_CHA',r'\}')

        #Palavras-chave
        self.lexer.add('IF',r'if')
        self.lexer.add('ELSE',r'else')
        self.lexer.add('WHILE',r'while')
        self.lexer.add('RETURN',r'return')
        self.lexer.add('FLOAT',r'float')
        self.lexer.add('CHAR',r'char')
        self.lexer.add('VOID',r'void')
        self.lexer.add('PRINT',r'prnt')
        self.lexer.add('INT',r'int')
        self.lexer.add('PROC',r'proc')
        self.lexer.add('VAR',r'var')


        self.lexer.add('FLOAT_L',r'[0-9]*,[0-9]+|[0-9]+,[0-9]*')
        self.lexer.add('INT_L',r'[0-9]+')
        self.lexer.add('CHAR_L',r'\"([0-9]|[a-zA-Z]|\n|\t|\s|:|\(|\)|,)+\"')

        self.lexer.ignore('\s+')
        #self.lexer.ignore('\n+')

	    # Identificador
        self.lexer.add('ID', r'[a-z]([a-zA-Z_]|[0-9])*')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
