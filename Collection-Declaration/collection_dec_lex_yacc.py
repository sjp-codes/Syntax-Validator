import ply.lex as lex
import ply.yacc as yacc

# list_variable = [list_values]
# tuple_variable = (tuple_values)
# dict_variable = {key:value}

tokens = (
    'ID',
    'NUMBER',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LBRACE',
    'RBRACE',
    'COMMA',
    'COLON',
    'STRING',
    'EQUAL'
)

t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_NUMBER = r'\d+'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_COLON = r':'
t_STRING = r'\".*?\"|\'[^\']*\''
t_EQUAL = r'='

t_ignore = ' \t\n'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

def p_collection_declaration(p):
    '''statement : ID EQUAL expression
                 | expression'''
    # p[0] = (p[1], p[3])  
    if len(p) == 4:  
        p[0] = (p[1], p[3])
    else:  
        p[0] = p[1]

def p_expression_type(p):
    '''expression : LBRACKET list_values RBRACKET
                  | LPAREN tuple_values RPAREN
                  | LBRACE dict_items RBRACE
                  | NUMBER
                  | STRING'''
    if len(p) == 2:
        p[0] = p[1]  
    else:
        p[0] = p[2]  

def p_list_values_dec(p):
    '''list_values : expression
                   | list_values COMMA expression'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]] 

def p_tuple_values_dec(p):
    '''tuple_values : expression
                    | tuple_values COMMA expression'''
    if len(p) == 2:
        p[0] = (p[1],)  
    else:
        p[0] = p[1] + (p[3],)

def p_dict_items_dec(p):
    '''dict_items : dict_item
                  | dict_items COMMA dict_item'''
    if len(p) == 2:
        p[0] = [p[1]] 
    else:
        p[0] = p[1] + [p[3]] 

def p_dict_item(p):
    '''dict_item : STRING COLON expression
                 | NUMBER COLON expression'''
    key = p[1][1:-1] if isinstance(p[1], str) else int(p[1]) 
    p[0] = (key, p[3])  

def p_error(p):
    print("Syntax error at '%s'" % p)

parser = yacc.yacc()

while True:
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

    if result is not None:
        print("Valid syntax")
        print(f"Parsed result: {result}")
    else:
        print("Syntax error")
