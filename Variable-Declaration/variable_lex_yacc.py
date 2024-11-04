import ply.lex as lex
import ply.yacc as yacc

# Simple Variable Declaration in Python
# variable_name = value 
# num = 10
# str = "name"

tokens = ('ID', 'STRING', 'EQUAL', 'NUMBER', 'TRUE', 'FALSE')

t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_STRING = r'\".*?\"|\'[^\']*\''
t_EQUAL = r'='
t_NUMBER = r'\d+'
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
    p[0] = (p[1], p[3])  

def p_expression_value(p):
    '''expression : NUMBER
                  | STRING
                  | TRUE
                  | FALSE'''
    if len(p) == 2:
        p[0] = p[1]  

def p_error(p):
    print("Syntax error at '%s'" % (p.value if p else "EOF"))
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
        print("You entered nothing, try again!")
        continue
    
    if s == '0':
        print("Exiting program")
        break

    result = parser.parse(s)

    if err == 0:
        print("Valid syntax")
        print(f"Parsed result: {result}")
    else:
        print("Syntax error")
