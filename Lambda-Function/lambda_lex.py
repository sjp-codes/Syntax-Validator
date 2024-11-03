import ply.lex as lex

# Define tokens
tokens = ('ID', 'LAMBDA', 'COLON', 'COMMA', 'MINUS', 'PLUS', 'MULTIPLY', 'DIVIDE', 'EQUAL', 'NUMBER', 'LPAREN', 'RPAREN')

t_ignore = ' \t'
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_LAMBDA = r'lambda'
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

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# Main input loop

while True:
    try:
            data = input("Enter a lambda expression: ")
            lexer.input(data)
            for tok in lexer:
                print(tok)
    except EOFError:
            break
