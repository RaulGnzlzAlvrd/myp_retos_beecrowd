def check_parenthesis_balance(expression):
    ''' Verifica que la expresión tenga paréntesis balanceados

    Parametres
    ----------
    expression: str
        La expresión a verificar

    Returns
    -------
    boolean
        True si tiene paréntesis balanceados, False e.o.c.
    '''
    counter = 0
    L_PAR = '('
    R_PAR = ')'
    for token in expression:
        if token == L_PAR:
            counter += 1
        elif token == R_PAR:
            counter -= 1
        if counter < 0:
            return False
    return counter == 0

def main():
    ''' Obtención de casos de prueba y ejecución de algoritmo principal

    Leemos los casos de prueba hasta un EOF e imprimimos el mensaje 
    adecuado para cada caso de prueba.
    '''
    while True:
        try:
            expression = input()
            if check_parenthesis_balance(expression):
                print("correct")
            else:
                print("incorrect")
        except EOFError:
            break

if __name__ == "__main__":
    ''' Punto de entrada del programa
    '''
    main()
