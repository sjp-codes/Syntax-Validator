import ply.lex as lex
import ply.yacc as yacc

# Simple Variable Declaration in Python
# variable_name = value 
# num = 10

tokens = ('ID','STRING','EQUAL','NUMBER','TRUE','FALSE')

t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_EQUAL = r'='
t_NUMBER = r'\d+'
t_STRING = r'\".*?\"|\'[^\']*\''
t_TRUE = r'true'
t_FALSE = r'false'

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

def p_variable_declaration(p):
    'statement : ID EQUAL expression'

def p_expression_value(p):
    '''expression : NUMBER
                  | STRING
                  | TRUE
                  | FALSE'''

def p_error(p):
    print("Syntax error")
    global err
    err = 1

parser = yacc.yacc()
while True:
    err = 0
    try:
        s = input('Enter the variable declaration statement or enter 0 to leave: ')
    except EOFError:
        break
    
    if not s: 
        err = 0
        print("You entered nothing, try again!")
        continue
    
    if s == '0':
        print("Exiting program")
        break

    result = parser.parse(s)

    # If there are no syntax errors, print valid syntax
    if err == 0:
        print("Valid syntax")