import ply.lex as lex
import ply.yacc as yacc

# variable = lambda arguments : expression
# lambda_cube = lambda y: y*y*y
# x = lambda a, b : a * b

tokens = (
    'ID',
    'LAMBDA', 
    'COLON', 
    'COMMA', 
    'MINUS', 
    'PLUS', 
    'MULTIPLY', 
    'DIVIDE', 
    'EQUAL', 
    'NUMBER', 
    'LPAREN', 
    'RPAREN'
)

t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_LAMBDA = r'lambda'
t_COLON = r':'
t_COMMA = r','
t_MINUS = r'-'
t_PLUS = r'\+'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_EQUAL = r'='
t_NUMBER = r'\d+'
t_LPAREN = r'\('
t_RPAREN = r'\)'

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

def p_lambda_function(p):
    '''lambda_fun : '''