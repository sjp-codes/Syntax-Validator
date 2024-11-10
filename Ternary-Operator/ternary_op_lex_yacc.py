import ply.lex as lex
import ply.yacc as yacc

# PYTHON SYNTAX FOR TERNARY OPERATOR
# syntax: result = true_value if condition else false_value

# 10 if 1 else 20 
# min = "a is minimum" if a < 10 else "b is minimum"

# LEXER

tokens = (
    'ID',
    'NUMBER',
    'STRING',
    'IF',
    'ELSE',
    'EQUALS',
    'LT',    
    'GT',    
    'LE',    
    'GE',    
    'EQ',   
    'NE',   
)

precedence = (
    ('nonassoc', 'LT', 'GT', 'LE', 'GE', 'EQ', 'NE'),  
    ('right', 'IF', 'ELSE'),  
    ('right', 'EQUALS'),  
)


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value == 'if':
        t.type = 'IF'
    elif t.value == 'else':
        t.type = 'ELSE'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\"[^\"]*\"'
    t.value = t.value[1:-1]  
    return t

t_EQUALS = r'='
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_EQ = r'=='
t_NE = r'!='
t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# PARSER
def p_statement(p):
    '''statement : assignment
                | expression'''
    p[0] = p[1]

def p_assignment(p):
    'assignment : ID EQUALS expression'
    symbol_table[p[1]] = p[3]
    p[0] = (p[1], p[3])

def p_expression(p):
    '''expression : ternary_expr
                 | comparison_expr
                 | primary'''
    p[0] = p[1]

def p_ternary_expr(p):
    'ternary_expr : primary IF comparison_expr ELSE expression'
    p[0] = p[1] if p[3] else p[5]

def p_comparison_expr(p):
    '''comparison_expr : primary LT primary
                      | primary GT primary
                      | primary LE primary
                      | primary GE primary
                      | primary EQ primary
                      | primary NE primary
                      | primary'''
    if len(p) == 4:
        if p[2] == '<':
            p[0] = p[1] < p[3]
        elif p[2] == '>':
            p[0] = p[1] > p[3]
        elif p[2] == '<=':
            p[0] = p[1] <= p[3]
        elif p[2] == '>=':
            p[0] = p[1] >= p[3]
        elif p[2] == '==':
            p[0] = p[1] == p[3]
        elif p[2] == '!=':
            p[0] = p[1] != p[3]
    else:
        p[0] = p[1]

def p_primary(p):
    '''primary : NUMBER
               | STRING
               | ID'''
    if isinstance(p[1], str) and p[1] in symbol_table and not isinstance(p[1], (int, float)):
        p[0] = symbol_table[p[1]]
    else:
        p[0] = p[1]

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}' (type: {p.type})")
    else:
        print("Syntax error at EOF")


lexer = lex.lex()

parser = yacc.yacc()

symbol_table = {}

while True:
    try:
        s = input('Enter ternary assignment expression (or "exit" to quit): ')
        if s.lower() == 'exit':
            break
    except EOFError:
        break

    result = parser.parse(s)
    if result is not None:
        print(f"Result: {result}")
        print(f"Symbol Table: {symbol_table}")