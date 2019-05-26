# Autor: Rafael Padilha
# Implementação de analizador lexico em python
# OLA MUNDO

# Função para buscar qual coluna da linha se inicia a palavra informada.
# Recebe a string linha e a string palavra, retorna um inteiro.
def busca_coluna(linha,palavra):
    lista_char = list(linha)
    a_c=0
    l_c=1
    p_t=[]
    for c in lista_char:
        a_c = a_c + 1
        if(c is ' '):
            p_t=[]
            l_c = a_c + 1
            
        else:
            p_t.append(c)
            teste = ''.join(p_t)
            if teste == palavra:
                #print("Debug: a:" + str(a_c) + ' l:' + str(l_c))
                return l_c

# Função principal do analizador lexico.
# Recebe duas strings com o nome do arquivo que contem as palavras aceitas pelo dicionario e tambem o nome do arquivo de entrada que vai verificar.
def anal_lexico(dict_file, entrada_file):
    dic = open(dict_file,'r').read().splitlines()
    entrada = open(entrada_file,'r').read().splitlines()

    l=0;
    for linha in entrada:
        l=l+1
        palavras = linha.split(' ')
        for palavra in palavras:
            if palavra not in dic:
                print("\'" + palavra + "\' não faz parte do dicionário. [Linha: " + str(l) + ', Coluna: ' + str(busca_coluna(linha,palavra)) + ']')
