import ply.lex as lex
import ply.yacc as yacc


#ternary expression
# syntax: result = true_value if condition else false_value

# example: 10 if 1 else 20 

#list of tokens
tokens = (
    'NUMBER',
    'IF',
    'ELSE',
)

#each token in expression
t_IF = r'if'
t_ELSE = r'else'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

#lexer part

lexer = lex.lex()

#parser part
def p_expression_ternary(p):
    'expression : expression IF expression ELSE expression'
    condition = p[3]
    true_value = p[1]
    false_value = p[5]
#ternary evaluatino
    p[0] = true_value if condition else false_value

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_error(p):
    print("Syntax error at '%s'" % p.value if p else "Syntax error at EOF")

parser = yacc.yacc()

while True:
    try:
        s = input('Enter ternary expression (or "exit" to quit): ')
        if s == 'exit':
            break
    except EOFError:
        break

    result = parser.parse(s)
    print(f"Result: {result}")
