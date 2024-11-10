import ply.lex as lex
import ply.yacc as yacc

# PYTHON SYNTAX FOR MAP FUNCTION
# variable = map(function, iterable)
# map(square, [1, 2, 3])
# result = map(lambda x: x * 2, [4, 5, 6])

# LEXER
tokens = (
    'MAP',
    'LAMBDA',
    'LPAREN',
    'RPAREN',
    'COLON',
    'COMMA',
    'IDENTIFIER',
    'EQUAL',
    'NUMBER',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'LEFT_BRACKET',
    'RIGHT_BRACKET',
)

reserved = {
    'map': 'MAP',
    'lambda': 'LAMBDA',
}

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COLON = r':'
t_COMMA = r','
t_EQUAL = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_LEFT_BRACKET = r'\['
t_RIGHT_BRACKET = r'\]'

t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# PARSER
def p_statement(p):
    '''statement : assignment
                 | map_expression'''
    p[0] = p[1]

def p_assignment(p):
    '''assignment : IDENTIFIER EQUAL map_expression'''
    p[0] = ('assignment', p[1], p[3])

def p_map_expression(p):
    '''map_expression : MAP LPAREN function COMMA iterable RPAREN'''
    p[0] = ('map', p[3], p[5])

def p_function(p):
    '''function : IDENTIFIER
                | lambda_func'''
    p[0] = p[1]

def p_lambda_func(p):
    '''lambda_func : LAMBDA arguments COLON expression'''
    p[0] = ('lambda', p[2], p[4])

def p_arguments(p):
    '''arguments : IDENTIFIER
                 | IDENTIFIER COMMA arguments'''
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
    '''factor : IDENTIFIER
              | NUMBER
              | LPAREN expression RPAREN'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]

def p_iterable(p):
    '''iterable : LEFT_BRACKET elements RIGHT_BRACKET'''
    p[0] = p[2]

def p_elements(p):
    '''elements : element
                | element COMMA elements'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_element(p):
    '''element : IDENTIFIER
               | NUMBER'''
    p[0] = p[1]

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()

while True:
    try:
        data = input("Enter a statement (or 'exit' to quit): ")
        if data.lower() == "exit":
            break
        result = parser.parse(data)
        if result:
            print("\nValid Syntax\n")
            print(f"Parsed result: {result}")
        else:
            print("Invalid syntax")
    except EOFError:
        break
    except KeyboardInterrupt:
        break
