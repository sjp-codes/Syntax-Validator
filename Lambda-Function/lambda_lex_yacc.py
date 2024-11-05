import ply.lex as lex
import ply.yacc as yacc

# PYTHON SYNTAX FOR LAMBDA FUNCTION
# variable = lambda arguments : expression
# lambda_cube = lambda y: y*y*y
# x = lambda a, b : a * b
# y = lambda a: a + 1

# LEXER
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

reserved = {
    'lambda': 'LAMBDA'
}

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

t_COLON = r':'
t_COMMA = r','
t_MINUS = r'-'
t_PLUS = r'\+'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_EQUAL = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# PARSER
def p_statement(p):
    '''statement : assignment
                | lambda_func'''
    p[0] = p[1]

def p_assignment(p):
    '''assignment : ID EQUAL lambda_func'''
    p[0] = ('assignment', p[1], p[3])

def p_lambda_func(p):
    '''lambda_func : LAMBDA arguments COLON expression'''
    p[0] = ('lambda', p[2], p[4])

def p_arguments(p):
    '''arguments : ID
                | ID COMMA arguments'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_expression(p):
    '''expression : term
                 | expression PLUS term
                 | expression MINUS term'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = ('binop', p[2], p[1], p[3])

def p_term(p):
    '''term : factor
            | term MULTIPLY factor
            | term DIVIDE factor'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = ('binop', p[2], p[1], p[3])

def p_factor(p):
    '''factor : ID
              | NUMBER
              | LPAREN expression RPAREN'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

while True:
    try:
        s = input('Enter the variable declaration statement or enter 0 to leave: ')
        if not s:
            print("You entered nothing, try again!")
            continue
        
        if s == '0':
            print("Exiting program")
            break
        
        result = parser.parse(s)
        if result is not None:
            print("\nValid syntax")
            print(f"Parsed result: {result}")
        else:
            print("\nInvalid syntax")
            
    except EOFError:
        break