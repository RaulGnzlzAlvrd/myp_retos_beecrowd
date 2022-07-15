def shunting_yard(expression):
    """
    Aplica el algoritmo Shunting Yard sobre expresiones
    matemáticas en notación infija. Regresa la expresión
    en notación postfija.

    params:
    expression: string

    returns: string la expresión postfija
    """
    operator_stack = []
    output = ""
    L_PAR = '('
    R_PAR = ')'
    operators = ['^', '*', '/', '+', '-']
    for symbol in expression:
        if symbol in operators:
            while len(operator_stack) > 0 and operator_stack[-1] != L_PAR and op_greater_than(operator_stack[-1], symbol):
                output += operator_stack.pop()
            operator_stack.append(symbol)
        elif symbol == L_PAR:
            operator_stack.append(symbol)
        elif symbol == R_PAR:
            while operator_stack[-1] != L_PAR:
                output += operator_stack.pop()
            operator_stack.pop()
        else:
            output += symbol
    for _ in range(len(operator_stack)):
        output += operator_stack.pop()
    return output

def op_greater_than(op1, op2):
    """
    Define precedencia y asociatividad sobre los símbolos op1, op2
    Regresa True si op1 tiene mayor o igual precedencia que op2

    params:
    op1: string
    op2: string

    returns boolean
    """
    if op1 == op2 == '^':
        return False
    if (op1 == '/' and op2 == '*') or (op1 == '-' and op2 == '+'):
        return True
    operators = ['^', '*', '/', '+', '-']
    return operators.index(op1) <= operators.index(op2)

def get_data():
    """
    Obtiene los casos de prueba del problema
    Regresa una lista con las cadenas de los casos de prueba

    returns: lista de string
    """
    numero_casos = int(input())
    casos = list()
    for _ in range(numero_casos):
        caso = input()
        casos.append(caso)
    return casos

def main():
    """
    Obtiene los casos de prueba e imprime la notación postfija
    de cada caso. Los casos deben estar en notación infija y se
    deben introducir primero el número de casos.
    """
    casos = get_data()
    for caso in casos:
        postfijo = shunting_yard(caso)
        print(postfijo)

if __name__ == "__main__":
    """
    Punto de entrada del programa
    """
    main()
