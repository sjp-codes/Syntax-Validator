import ply.lex as lex
import ply.yacc as yacc

# Define the lexer
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

# Build the lexer
lexer = lex.lex()

# Define the grammar for parsing variable declarations
def p_statement_assign(p):
    'statement : ID EQUAL expression'
    p[0] = (p[1], p[3])  # Return a tuple of (variable_name, value)

def p_expression_list(p):
    'expression : LBRACKET list_values RBRACKET'
    p[0] = p[2]  # The value is the list of values

def p_expression_tuple(p):
    'expression : LPAREN tuple_values RPAREN'
    p[0] = p[2]  # The value is the tuple of values

def p_expression_dict(p):
    'expression : LBRACE dict_items RBRACE'
    p[0] = {key: value for key, value in p[2]}  # Construct the dictionary

def p_list_values_single(p):
    'list_values : expression'
    p[0] = [p[1]]  # Single value in the list

def p_list_values_multiple(p):
    'list_values : list_values COMMA expression'
    p[0] = p[1] + [p[3]]  # Combine the list of values

def p_tuple_values_single(p):
    'tuple_values : expression'
    p[0] = (p[1],)  # Single value in the tuple

def p_tuple_values_multiple(p):
    'tuple_values : tuple_values COMMA expression'
    p[0] = p[1] + (p[3],)  # Combine values into a tuple

def p_dict_items_single(p):
    'dict_items : dict_item'
    p[0] = [p[1]]  # Single item in the dictionary

def p_dict_items_multiple(p):
    'dict_items : dict_items COMMA dict_item'
    p[0] = p[1] + [p[3]]  # Combine dictionary items

def p_dict_item(p):
    'dict_item : STRING COLON expression'
    p[0] = (p[1][1:-1], p[3])  # Remove quotes from string keys

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = int(p[1])  # Convert to integer

def p_expression_id(p):
    'expression : ID'
    p[0] = p[1]  # Return the identifier as is

def p_expression_string(p):
    'expression : STRING'
    p[0] = p[1][1:-1]  # Remove quotes from string

def p_error(p):
    print("Syntax error at '%s'" % p)

# Build the parser
parser = yacc.yacc()

# Test the parser
input_data = '''
my_list = [1, 2, 3]
my_tuple = (4, 5)
my_dict = {"key1": "value1", "key2": 2}
my_dicttt = {1:2,3:5}
'''

for line in input_data.strip().split('\n'):
    result = parser.parse(line.strip())
    print(result)
