import ply.lex as lex

# lambda arguments : expression
# x = lambda a, b : a * b

tokens = ('ID','LAMBDA','COLON','COMMA','MINUS','PLUS','MULTIPLY','DIVIDE','EQUAL','NUMBER','ARROW','LPAREN','RPAREN')

t_ignore =' \t'
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_LAMBDA = r'lambda'
t_COLON = r':'
t_COMMA = r','
t_MINUS = r'-'
t_PLUS = r'\+'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_EQUAL = r'='
t_ARROW = r'->'
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

data = '''
lambda x, y: x + y
lambda a, b: a = b + 1
lambda c: (c * 2) -> c / 2
'''

lexer.input(data)

for tok in lexer:
    print(tok)