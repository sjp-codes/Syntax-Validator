import ply.lex as lex
import ply.yacc as yacc

# Tokens
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

# Parsing rules
def p_lambda_function(p):
    '''lambda_fun : LAMBDA arguments COLON expression'''
    p[0] = {'type': 'lambda', 'args': p[2], 'body': p[4]}  # Create a dictionary to represent the lambda function

def p_arguments_single(p):
    '''arguments : ID'''
    p[0] = [p[1]]  # Single argument

def p_arguments_multiple(p):
    '''arguments : ID COMMA arguments'''
    p[0] = [p[1]] + p[3]  # List of arguments

def p_expression_id(p):
    '''expression : ID'''
    p[0] = {'type': 'id', 'value': p[1]}  # Identifier expression

def p_expression_number(p):
    '''expression : NUMBER'''
    p[0] = {'type': 'number', 'value': int(p[1])}  # Number expression

def p_expression_arithmetic(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression MULTIPLY expression
                  | expression DIVIDE expression'''
    p[0] = {'type': 'binary_op', 'op': p[2], 'left': p[1], 'right': p[3]}  # Binary operation

def p_error(p):
    print("Syntax error at '%s'" % p)

# Build the parser
parser = yacc.yacc()

# Example usage
while True:
    try:
        s = input('Enter a lambda function or enter 0 to leave: ')
    except EOFError:
        break
    
    if s == '0':
        print("Exiting program")
        break

    result = parser.parse(s)
    if result:
        print("Parsed result:", result)
    else:
        print("Syntax error")
