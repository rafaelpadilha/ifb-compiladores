from lexer_a import Lexer
from parser2 import Parser

entrada_1 = """
proc main()
{
    var n, nRebuilt - int;
    n := 51423;
    
    nRebuilt := (n / 2) * 2;
    
    if(n = nRebuilt)
        prnt('P', 'A', 'R');
    else
        prnt('I', 'M', 'P', 'A', 'R');
    
}
"""

text_input = """

var n, soma - int;

proc main()
{
    var result - int;
    
    result := soma(9)primeirosImpares();
    
    prnt(result);
}

proc soma(n -int)primeirosImpares() - int
{
    var i, proxImpar, resultado - int;
    
    resultado := 0;
    i := 0;
    
    while(i < n){
        proxImpar := 2*i + 1;
        resultado := resultado + proxImpar;
        i := i + 1;
    }
    
    return resultado;
    
}
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)


#for token in tokens:
#    print(token)
    
pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()

