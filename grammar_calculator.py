import ply.lex as lex
import ply.yacc as yacc
import math

# Tokens
tokens = (
    'NUMERO',
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'PARENTESIS_IZQ',
    'PARENTESIS_DER',
    'POTENCIA',
    'LOGARITMO',
)

# Reglas para los tokens
t_MAS = r'\+'
t_MENOS = r'-'
t_POR = r'\*'
t_DIVIDIDO = r'/'
t_PARENTESIS_IZQ = r'\('
t_PARENTESIS_DER = r'\)'
t_POTENCIA = r'\^'
t_LOGARITMO = r'log10'

def t_NUMERO(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# Reglas de la gramática
def p_expresion_binaria(p):
    '''expresion : expresion MAS termino
                 | expresion MENOS termino
                 | expresion POTENCIA termino'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '^':
        p[0] = p[1] ** p[3]

def p_expresion_termino(p):
    'expresion : termino'
    p[0] = p[1]

def p_termino_binario(p):
    '''termino : termino POR factor
               | termino DIVIDIDO factor'''
    if p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]

def p_termino_factor(p):
    'termino : factor'
    p[0] = p[1]

def p_factor_numero(p):
    'factor : NUMERO'
    p[0] = p[1]

def p_factor_expresion(p):
    'factor : PARENTESIS_IZQ expresion PARENTESIS_DER'
    p[0] = p[2]

def p_factor_logaritmo(p):
    'factor : LOGARITMO PARENTESIS_IZQ expresion PARENTESIS_DER'
    p[0] = math.log10(p[3])

def p_error(p):
    print("Error de sintaxis")

parser = yacc.yacc()

def evaluar_expresion(expresion):
    try:
        return parser.parse(expresion)
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    while True:
        try:
            s = input('calc > ')
        except EOFError:
            break
        if not s:
            continue
        print(evaluar_expresion(s))