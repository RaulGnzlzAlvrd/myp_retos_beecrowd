import random

from main import sort_by_function

def test_sort_by_function():
    """
    Testea la funcionalidad principal del programa usando las cadenas
    que salen en el reto.
    """
    casos_prueba = [
            {"entrada": "Top Coder comp Wedn at midnight",
             "salida": "midnight Coder comp Wedn Top at"},
            {"entrada": "one three five",
             "salida": "three five one"},
            {"entrada": "I love Cpp",
             "salida": "love Cpp I"},
            {"entrada": "sj a sa df r e w f d s a v c x z sd fd",
             "salida": "sj sa df sd fd a r e w f d s a v c x z"},
    ]
    for caso in casos_prueba:
        lista = caso["entrada"].split(" ")
        obtenido = sort_by_function(lista, len)
        esperado = caso["salida"].split(" ")
        assert esperado == obtenido, f"Falló en caso {esperado} != {obtenido}"

if __name__ == "__main__":
    test_sort_by_function()
