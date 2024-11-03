import ply.yacc as yacc
from lambda_lex import tokens

flag = 0

def p_lambda_function(p):
    '''
    lambda_function : LAMBDA parameters COLON expression
    '''
    p[0] = ('lambda', p[2], p[4])

def p_parameters(p):
    '''
    parameters : ID COMMA parameters
               | ID
               | 
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    elif len(p) == 4:
        p[0] = [p[1]] + p[3]
    else:
        p[0] = []

def p_expression_number(p):
    '''
    expression : NUMBER
    '''
    p[0] = p[1]

def p_expression_id(p):
    '''
    expression : ID
    '''
    p[0] = p[1]

def p_error(p):
    print("Syntax error in lambda expression!")
    global flag
    flag = 1

parser = yacc.yacc()

while True:
    flag = 0
    try:
        s = input("Enter a lambda expression: ")
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(s)
    if flag == 0:
        print("Parsed lambda expression:", result)