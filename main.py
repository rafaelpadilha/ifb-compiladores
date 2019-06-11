from lexer_a import Lexer
from parser2 import Parser
import Tkinter as tk



window = tk.Tk()

window.title("Compilador")

window.geometry('1200x600')
left = tk.Frame(window)

var_lex = tk.StringVar()
var_sint = tk.StringVar()
token_list = tk.StringVar()
var_lex.set('Nenhum Erro Lexico')
var_sint.set('Nenhum Erro Sintatico')
token_list.set('Nenhum Token')
# ScrolledTxt

textContainer = tk.Frame(left, borderwidth=0, relief="sunken")
text = tk.Text(textContainer, width=50, height=25, wrap="none", borderwidth=0)
textVsb = tk.Scrollbar(textContainer, orient="vertical", command=text.yview)
textHsb = tk.Scrollbar(textContainer, orient="horizontal", command=text.xview)
text.configure(yscrollcommand=textVsb.set, xscrollcommand=textHsb.set)

text.grid(row=0, column=0, sticky="nsew")
textVsb.grid(row=0, column=1, sticky="ns")
textHsb.grid(row=1, column=0, sticky="ew")

textContainer.grid_rowconfigure(0, weight=1)
textContainer.grid_columnconfigure(0, weight=1)

left.pack(side='left',expand=True,fill='both')
textContainer.pack(side='left', expand=True,fill='both')


#

# Tokens

right = tk.Frame(window)

tokens_t = tk.Label(right, text="Tokens")
tokens = tk.Label(right, textvariable=token_list)

right.pack(side='right', expand=True ,fill='both')
tokens_t.pack(side='top')
tokens.pack()

bottom = tk.Frame(window)

er_lex = tk.Label(bottom, textvariable=var_lex)
er_sint = tk.Label(bottom, textvariable=var_sint)
def callback_btn():
    entrada = text.get("1.0",'end-1c')
    lexer = Lexer().get_lexer()
    tokens=[]
    try:
        tokens = lexer.lex(entrada)
        print(str(entrada))
        o_t = list(tokens)
        tkns=''
        for i in o_t:
            tkns += str(i) + '\n'
        token_list.set(tkns)
        print('A>'+ tkns)
    except Exception as e:
        var_lex.set('Erro lexico: ' + str(e))
        print(e)
        
    try:
        pg = Parser()
        pg.parse()
        parser = pg.get_parser()
        parser.parse(tokens).eval()
    except Exception as e:
        var_sint.set('Erro sintatico: '+str(e))
        print(e)

botao = tk.Button(bottom, text='Go', command=callback_btn)

bottom.pack(side='bottom')
er_lex.pack(side='left',padx = 100,pady = 250, expand=True ,fill='both')
botao.pack(side='right')
er_sint.pack(side='right', padx = 100,pady = 250, expand=True ,fill='both')


window.mainloop()




for token in tokens:
    print(token)
    


