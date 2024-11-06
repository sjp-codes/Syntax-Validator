import ply.lex as lex
import ply.yacc as yacc

#this is our lexer 
tokens = (
    'MAP',
    'LPAREN',
    'RPAREN',
    'COMMA',
    'IDENTIFIER',
    'EQUAL',
)

reserved = {
    'map': 'MAP',
}

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_EQUAL = r'='

t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

#this is our parser
def p_statement(p):
    '''statement : assignment
                | map_expression'''
    p[0] = p[1]

def p_assignment(p):
    '''assignment : IDENTIFIER EQUAL map_expression'''
    p[0] = ('assignment', p[1], p[3])

def p_map_expression(p):
    '''map_expression : MAP LPAREN IDENTIFIER COMMA IDENTIFIER RPAREN'''
    p[0] = ('map', p[3], p[5])

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()

#for user input
while True:
    try:
        data = input("Enter a statement (or 'exit' to quit): ")
        if data.lower() == "exit":
            break
        result = parser.parse(data)
        if result:
            print(f"Parsed result: {result}")
        else:
            print("Invalid syntax")
    except EOFError:
        break
    except KeyboardInterrupt:
        break