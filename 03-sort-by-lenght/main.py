def sort_by_function(data, function, descend=True):
    """
    Función principal, toma de entrada una lista y una función en la
    que se evaluan los elementos de la lista.
    Regresa la lista ordenada en forma descendente.

    params:
    data: lista de A
    funciton: función a -> comparable
    descend: booleano

    return:
    lista de A
    """
    f_data = [function(d) for d in data]
    sorted_data, _ = sort_by_function_aux(data, f_data, descend)
    return sorted_data

def sort_by_function_aux(data, f_data, descend):
    """
    Función auxiliar de sort_by_function
    Acepta una lista de datos y una lista f_data del mismo
    tamaño que data.
    Regresa la lista f_data ordenada y la lista data la regresa
    acomodada según el orden de f_data

    params:
    data: lista de A
    f_data: lista de comparable
    descend: booleano

    return tupla con data ordenada según f_data
    """
    number_elements = len(data)
    if number_elements <= 1:
        return data, f_data
    middle_point = number_elements // 2
    first_data, first_f_data = sort_by_function_aux(data[:middle_point], f_data[:middle_point], descend)
    second_data, second_f_data = sort_by_function_aux(data[middle_point:], f_data[middle_point:], descend)
    return sort_ordered_lists(first_data, second_data, first_f_data, second_f_data, descend)

def sort_ordered_lists(data1, data2, f_data1, f_data2, descend=True):
    """
    Regresa una lista ordenada con los elemenetos de
    f_data1, fdata2. Aplica el paso recursivo de merge sort pero
    ordena data1, data2 según el orden final de f_data1, f_data2

    params:
    data1: lista de A
    data2: lista de A
    f_data1: lista de comparable
    f_data2: lista de comparable
    descend: boolean

    returns lista de A, lista de comparable
    """
    new_data = list()
    new_f_data = list()
    i = 0
    j = 0
    d1_size = len(data1)
    d2_size = len(data2)
    if descend:
        comparision = lambda x,y: x >= y
    else:
        comparision = lambda x,y: x <= y
    for _ in range(d1_size + d2_size):
        condition = (j == d2_size) or (i != d1_size and comparision(f_data1[i], f_data2[j]))
        if condition:
            new_data.append(data1[i])
            new_f_data.append(f_data1[i])
            i += 1
        else:
            new_data.append(data2[j])
            new_f_data.append(f_data2[j])
            j += 1
    return new_data, new_f_data

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
    Punto de entrada del programa. Manda a llamar las dempas funcionalidades
    """
    casos = get_data()
    separator = " "
    for caso in casos:
        ordenados = sort_by_function(caso.split(separator), len)
        formateado = separator.join(ordenados)
        print(formateado)
    return

if __name__ == "__main__":
    main()
